import spacy
from spacy.tokens import Doc
import json
import entity_retokenizer
import citation_component
import description_extractor
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, DCTERMS
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (change this for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)


class TextRequest(BaseModel):
    text: str


nlp = spacy.load("en_core_web_sm")

EX = Namespace("http://example.org/disorder/")


@app.post("/extract_triples/")
def extract_triples(request: TextRequest):
    """Extract disorder triples and return as a structured response"""
    doc = nlp(request.text)

    print(type(nlp))
    print(dir(nlp))

    if "citation_component" not in nlp.pipe_names:
        nlp.add_pipe("citation_component", after="ner")

    if "merge_phrases" not in nlp.pipe_names:
        nlp.add_pipe("entity_retokenizer_component", name='merge_phrases', after='citation_component')

    with open('disorder_patterns.json', 'r') as file:
        disorder_patterns = json.load(file)

    # Add the EntityRuler to the pipeline
    if "entity_ruler" not in nlp.pipe_names:
        ruler = nlp.add_pipe('entity_ruler', after="ner")
        ruler.add_patterns(disorder_patterns)

    if "disorder_extractor" not in nlp.pipe_names:
        Doc.set_extension("disorder_descriptions", default=[], force=True)
        nlp.add_pipe("disorder_extractor", after="merge_phrases")

    print(nlp.pipe_names)

    g = Graph()

    g.bind("ex", EX)
    g.bind("rdfs", RDFS)
    g.bind("dct", DCTERMS)

    # Convert extracted disorders & descriptions into RDF triples
    for disorder, description in doc._.disorder_descriptions:
        disorder_uri = URIRef(EX + disorder.replace(" ", "_"))  # Create a unique URI
        g.add((disorder_uri, RDFS.label, Literal(disorder)))  # Add disorder label
        g.add((disorder_uri, DCTERMS.description, Literal(description)))  # Add description

    # Print RDF graph in Turtle format
    print(g.serialize(format="turtle"))

    return g.serialize(format="turtle")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    # main()
