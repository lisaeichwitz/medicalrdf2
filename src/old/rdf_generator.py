from rdflib import Graph, Namespace, Literal, RDF, RDFS, URIRef


def load_rdf_schema(file_path):
    g = Graph()
    g.parse(file_path, format="turtle")
    return g


# Load the schema
schema_graph = load_rdf_schema("../schemas/medical_schema.ttl")

# Print all triples
for subj, pred, obj in schema_graph:
    print(subj, pred, obj)

EX = Namespace("http://example.org/ontology#")


def generate_rdf(entities):
    """Generate RDF triples following the medical schema."""
    g = Graph()
    g.bind("ex", EX)

    disorder = URIRef(EX.PanicAttack)
    g.add((disorder, RDF.type, EX.Disorder))

    for entity, label in entities.items():
        symptom = URIRef(EX + entity.replace(" ", ""))
        g.add((symptom, RDF.type, EX.Symptom))
        g.add((disorder, EX.hasSymptom, symptom))

    return g.serialize(format="turtle")


# Example use case
entities = {"Shortness of Breath": "Symptom", "Chest Pain": "Symptom"}
rdf_output = generate_rdf(entities)
print(rdf_output)
