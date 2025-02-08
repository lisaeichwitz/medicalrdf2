from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Span


@Language.factory("citation_component")
def create_citation_component(nlp, name):
    """Factory function to create the citation matcher component"""
    matcher = Matcher(nlp.vocab)

    # Define the pattern for APA-style citations (e.g., (American Psychiatric Association, 2013))
    pattern = [
        {"ORTH": "("},  # Opening parenthesis
        {"IS_TITLE": True, "OP": "+"},  # One or more capitalized words
        {"TEXT": ","},  # Comma
        {"TEXT": {"REGEX": r"\d{4}"}},  # Four-digit year
        {"ORTH": ")"},  # Closing parenthesis
    ]

    matcher.add("CITATION", [pattern])

    def citation_component(doc):
        """Custom pipeline component to detect APA citations."""
        matches = matcher(doc)
        new_spans = [Span(doc, start, end, label="CITATION") for _, start, end in matches]

        # Remove conflicting entities (ORG, DATE) that overlap with citations
        existing_spans = []
        for ent in doc.ents:
            if not any(token in ent for span in new_spans for token in span):
                existing_spans.append(ent)

        # Merge new citations with filtered entities
        doc.set_ents(existing_spans + new_spans, default="unmodified")
        return doc

    return citation_component
