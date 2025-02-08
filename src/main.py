import spacy
from spacy.tokens import Doc
import json
import entity_retokenizer
import citation_component
import description_extractor


def main():
    """Main execution function for NLP pipeline and RDF generation."""
    with open('disorder_patterns.json', 'r') as file:
        disorder_patterns = json.load(file)

    nlp = spacy.load("en_core_web_sm")

    if "citation_component" not in nlp.pipe_names:
        nlp.add_pipe("citation_component", after="ner")

    nlp.add_pipe("entity_retokenizer_component", name='merge_phrases', after='citation_component')

    # Add the EntityRuler to the pipeline
    ruler = nlp.add_pipe('entity_ruler', after="ner")
    ruler.add_patterns(disorder_patterns)

    Doc.set_extension("disorder_descriptions", default=[], force=True)
    nlp.add_pipe("disorder_extractor", after="merge_phrases")

    with open("../data/panic_attacks.txt", "r") as f:
        text = f.read()

    print(text)

    doc = nlp(text)

    # Print detected entities
    for ent in doc.ents:
        print(ent.text, ent.label_)

    for disorder, description in doc._.disorder_descriptions:
        print(f"Disorder: {disorder}\nDescription: {description}\n")


if __name__ == "__main__":
    main()
