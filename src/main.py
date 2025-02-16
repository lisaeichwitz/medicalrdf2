import json

import spacy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDFS, DCTERMS
from spacy.tokens import Doc

import citation_component
import citation_extractor
import description_extractor
import diagnosis_extractor
import entity_retokenizer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


nlp = spacy.load("en_core_web_sm")

EX = Namespace("http://example.org/disorder/")


@app.post("/extract_triples/")
def extract_triples(request: TextRequest):
    """Extract disorder triples and return as a structured response"""
    doc = nlp(request.text)

    if "citation_component" not in nlp.pipe_names:
        nlp.add_pipe("citation_component", after="ner")

    if "merge_phrases" not in nlp.pipe_names:
        nlp.add_pipe("entity_retokenizer_component", name='merge_phrases', after='citation_component')

    with open('disorder_patterns.json', 'r') as file:
        disorder_patterns = json.load(file)

    if "entity_ruler" not in nlp.pipe_names:
        ruler = nlp.add_pipe('entity_ruler', after="ner")
        ruler.add_patterns(disorder_patterns)

    if "description_extractor" not in nlp.pipe_names:
        Doc.set_extension("disorder_descriptions", default=[], force=True)
        nlp.add_pipe("description_extractor", after="merge_phrases")

    if "citation_extractor" not in nlp.pipe_names:
        Doc.set_extension("disorder_citations", default=[], force=True)
        nlp.add_pipe("citation_extractor", after="merge_phrases")

    if "diagnosis_extractor" not in nlp.pipe_names:
        Doc.set_extension("disorder_diagnoses", default=[], force=True)
        nlp.add_pipe("diagnosis_extractor", after="merge_phrases")

    g = Graph()
    g.bind("ex", EX)
    g.bind("rdfs", RDFS)
    g.bind("dct", DCTERMS)

    for disorder, description in doc._.disorder_descriptions:
        disorder_uri = URIRef(EX + disorder.replace(" ", "_"))
        g.add((disorder_uri, RDFS.label, Literal(disorder)))
        g.add((disorder_uri, DCTERMS.description, Literal(description)))

        for diag_term, diagnosis in doc._.disorder_diagnoses:
            if diag_term == "diagnosis":
                g.add((disorder_uri, URIRef(EX + "diagnosis"), Literal(diagnosis)))

        for dis, citation in doc._.disorder_citations:
            if dis == disorder:
                g.add((disorder_uri, URIRef(EX + "citation"), Literal(citation)))

    return {"rdf_data": g.serialize(format="xml")}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
