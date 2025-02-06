from rdflib import Graph, Namespace, Literal, RDF, RDFS, URIRef

EX = Namespace("http://example.org/ontology#")


class RDFManager:
    """Handles RDF schema loading and RDF triple generation."""

    def __init__(self, schema_path):
        """Initialize RDF graph and load the schema."""
        self.graph = Graph()
        self.schema_path = schema_path
        self.load_schema()

    def load_schema(self):
        """Load RDF schema from a Turtle file."""
        self.graph.parse(self.schema_path, format="turtle")

    def generate_rdf(self, disorder_name, symptoms):
        """Generate RDF triples using predefined schema."""
        disorder_uri = URIRef(EX + disorder_name.replace(" ", ""))
        self.graph.add((disorder_uri, RDF.type, EX.Disorder))

        for symptom in symptoms:
            symptom_uri = URIRef(EX + symptom.replace(" ", ""))
            self.graph.add((symptom_uri, RDF.type, EX.Symptom))
            self.graph.add((disorder_uri, EX.hasSymptom, symptom_uri))

        return self.graph.serialize(format="turtle")
