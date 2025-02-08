import spacy
from spacy.pipeline import EntityRuler


class EntityExtractor:
    """Extract named entities using a custom rule-based entity recognizer."""

    def __init__(self, model="en_core_web_sm", patterns_file="../data/patterns.json"):
        self.nlp = spacy.load(model)
        self.add_custom_entities(patterns_file)

    def add_custom_entities(self, patterns_file):
        """Load custom named entity patterns into SpaCy pipeline."""
        ruler = self.nlp.add_pipe("entity_ruler", before="ner")
        import json
        with open(patterns_file, "r") as file:
            patterns = json.load(file)
        ruler.add_patterns(patterns)

    def extract_entities(self, text):
        """Extract entities from text."""
        doc = self.nlp(text)
        return {ent.text: ent.label_ for ent in doc.ents}


# Example usage
if __name__ == "__main__":
    extractor = EntityExtractor()
    text = "The patient experienced shortness of breath and was diagnosed with Panic Attack."
    entities = extractor.extract_entities(text)
    print(entities)  # Output: {'shortness of breath': 'SYMPTOM', 'Panic Attack': 'DISORDER'}
