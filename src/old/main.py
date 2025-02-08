# from preprocess import preprocess_text
# from entity_extraction import extract_entities
# from rdf_generator import generate_rdf
#
#
# def main():
#     with open("../data/panic_attacks.txt", "r") as file:
#         text = file.read()
#
#     tokens = preprocess_text(text)
#     entities = extract_entities(text)
#     rdf_output = generate_rdf(entities)
#
#     print("Extracted Tokens:", tokens)
#     print("Extracted Entities:", entities)
#     print("Generated RDF Triples:")
#     print(rdf_output)
#
#
# if __name__ == "__main__":
#     main()

# from nlp_pipeline import NLPPipeline
# from rdf_manager import RDFManager
#
# # File paths
# SCHEMA_PATH = "../schemas/medical_schema.ttl"
# INPUT_TEXT_PATH = "../data/panic_attacks.txt"
#
#
# def main():
#     """Main execution function for NLP pipeline and RDF generation."""
#     nlp_pipeline = NLPPipeline()
#     rdf_manager = RDFManager(SCHEMA_PATH)
#
#     # Read input text
#     with open(INPUT_TEXT_PATH, "r") as file:
#         text = file.read()
#
#     # NLP Processing
#     tokens = nlp_pipeline.preprocess_text(text)
#     entities = nlp_pipeline.extract_entities(text)
#
#     # Extract disorder & symptoms
#     disorder_name = "PanicAttack"
#     symptoms = [entity for entity, label in entities.items() if label in ["SYMPTOM", "DIAGNOSIS"]]
#
#     # Generate RDF
#     rdf_output = rdf_manager.generate_rdf(disorder_name, symptoms)
#
#     print("Extracted Tokens:", tokens)
#     print("Extracted Entities:", entities)
#     print("Generated RDF Triples:")
#     print(rdf_output)
#
#
# if __name__ == "__main__":
#     main()


from nlp_pipeline import NLPPipeline
from rdf_manager import RDFManager
from entity_extraction import EntityExtractor

SCHEMA_PATH = "../schemas/medical_schema.ttl"
INPUT_TEXT_PATH = "../data/panic_attacks.txt"


def main():
    """Main execution function for NLP pipeline and RDF generation."""
    nlp_pipeline = NLPPipeline()
    rdf_manager = RDFManager(SCHEMA_PATH)
    entity_extractor = EntityExtractor()

    # Read input text
    with open(INPUT_TEXT_PATH, "r") as file:
        text = file.read()

    # NLP Processing
    tokens = nlp_pipeline.preprocess_text(text)
    entities = entity_extractor.extract_entities(text)

    # Extract disorder & symptoms
    disorder_name = "PanicAttack"
    symptoms = [entity for entity, label in entities.items() if label == "SYMPTOM"]

    # Generate RDF
    rdf_output = rdf_manager.generate_rdf(disorder_name, symptoms)

    print("Extracted Tokens:", tokens)
    print("Extracted Entities:", entities)
    print("Generated RDF Triples:")
    print(rdf_output)


if __name__ == "__main__":
    main()
