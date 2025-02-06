import spacy
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


class NLPPipeline:
    """Pipeline for processing medical text using NLP techniques."""

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def preprocess_text(self, text):
        """Normalize text by lowercasing and removing stopwords."""
        doc = self.nlp(text.lower())
        tokens = [token.lemma_ for token in doc if token.is_alpha and token.text not in stopwords.words('english')]
        return tokens

    def extract_entities(self, text):
        """Extract named entities from text using SpaCy."""
        doc = self.nlp(text)
        return {ent.text: ent.label_ for ent in doc.ents}
