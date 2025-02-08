import spacy


class CustomNER:
    """Loads and uses the custom trained NER model."""

    def __init__(self, model_path="../models/custom_ner"):
        self.nlp = spacy.load(model_path)

    def extract_entities(self, text):
        """Extract entities from text using the trained model."""
        doc = self.nlp(text)
        return {ent.text: ent.label_ for ent in doc.ents}


# Example usage
if __name__ == "__main__":
    ner = CustomNER()
    text = "Patient was diagnosed with Panic Attack and treated with cognitive behavioral therapy."
    print(ner.extract_entities(text))
