from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Span


@Language.factory("citation_component")
def create_citation_component(nlp, name):
    """Factory function to create the citation matcher component"""
    matcher = Matcher(nlp.vocab)

    # # Define the pattern for APA-style citations
    # citation_pattern = [
    #     {"ORTH": "("},  # Opening parenthesis
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "+"},  # First author or organization name
    #     {"TEXT": ","},  # Comma separator
    #     {"TEXT": {"REGEX": r"(\s*et al\.\s*)?"}, "OP": "?"},  # Optional "et al."
    #     {"TEXT": {"REGEX": r"\d{4}"}},  # Four-digit year
    #     {"ORTH": ")"},  # Closing parenthesis
    # ]
    #
    # # Extend pattern to support multiple authors with ampersand or commas
    # extended_citation_pattern = [
    #     {"ORTH": "("},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "+"},  # First author or organization
    #     {"TEXT": ",", "OP": "?"},  # Optional comma
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},  # Other authors
    #     {"TEXT": {"REGEX": r"(&|and|,)"}, "OP": "*"},  # "&", "and", or comma
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},  # Last author before year
    #     {"TEXT": ","},  # Comma before year
    #     {"TEXT": {"REGEX": r"\d{4}"}},  # Four-digit year
    #     {"ORTH": ")"}
    # ]
    #
    # # Extend further for multiple citations inside parentheses
    # multi_citation_pattern = [
    #     {"ORTH": "("},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "+"},
    #     {"TEXT": ",", "OP": "?"},
    #     {"TEXT": {"REGEX": r"(&|and|,|et al\.)"}, "OP": "*"},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ","},
    #     {"TEXT": {"REGEX": r"\d{4}"}},
    #     {"TEXT": ";", "OP": "*"},  # Handles multiple citations in one parentheses
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ",", "OP": "?"},
    #     {"TEXT": {"REGEX": r"(&|and|,|et al\.)"}, "OP": "*"},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ","},
    #     {"TEXT": {"REGEX": r"\d{4}"}},
    #     {"ORTH": ")"}
    # ]

    # citation_pattern = [
    #     {"ORTH": "("},  # Opening parenthesis
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}},  # First author or organization
    #     {"TEXT": ",", "OP": "?"},  # Optional comma after first name
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},  # Additional author names
    #     {"TEXT": ",", "OP": "*"},  # Optional commas
    #     {"TEXT": {"REGEX": r"(&|and|et al\.)"}, "OP": "?"},  # "&", "and", or "et al."
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "?"},  # Last author
    #     {"TEXT": ","},  # Comma before the year
    #     {"TEXT": {"REGEX": r"\d{4}"}},  # Four-digit year
    #     {"ORTH": ")"},  # Closing parenthesis
    # ]
    #
    # # Extend pattern to support multiple citations within parentheses
    # multi_citation_pattern = [
    #     {"ORTH": "("},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}},
    #     {"TEXT": ",", "OP": "?"},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ",", "OP": "*"},
    #     {"TEXT": {"REGEX": r"(&|and|et al\.|,)"}, "OP": "*"},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ","},
    #     {"TEXT": {"REGEX": r"\d{4}"}},
    #     {"TEXT": ";", "OP": "*"},  # Handles multiple citations in one parentheses
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ",", "OP": "?"},
    #     {"TEXT": {"REGEX": r"(&|and|et al\.|,)"}, "OP": "*"},
    #     {"TEXT": {"REGEX": r"[A-Z][a-zA-Z-]*"}, "OP": "*"},
    #     {"TEXT": ","},
    #     {"TEXT": {"REGEX": r"\d{4}"}},
    #     {"ORTH": ")"}
    # ]
    # matcher.add("CITATION", [citation_pattern, multi_citation_pattern])

    # def citation_component(doc):
    #     """Custom pipeline component to detect APA citations."""
    #     matches = matcher(doc)
    #     new_spans = [Span(doc, start, end, label="CITATION") for _, start, end in matches]
    #
    #     # Remove conflicting entities (ORG, DATE) that overlap with citations
    #     existing_spans = []
    #     for ent in doc.ents:
    #         if not any(token in ent for span in new_spans for token in span):
    #             existing_spans.append(ent)
    #
    #     # Merge new citations with filtered entities
    #     doc.set_ents(existing_spans + new_spans, default="unmodified")
    #
    #     print(doc.ents)
    #
    #     return doc
    #
    # return citation_component

    # Define APA-style citation patterns
    single_author_pattern = [
        [{"ORTH": "("}, {"IS_ALPHA": True, "OP": "+"}, {"ORTH": ","}, {"IS_DIGIT": True}, {"ORTH": ")"}]]

    multiple_authors_pattern = [[
        {"ORTH": "("},
        {"IS_ALPHA": True, "OP": "+"},
        {"ORTH": ","},
        {"IS_ALPHA": True, "OP": "*"},
        {"ORTH": "&"},
        {"IS_ALPHA": True, "OP": "+"},
        {"ORTH": ","},
        {"IS_DIGIT": True},
        {"ORTH": ")"}
    ]]

    et_al_pattern = [[{"ORTH": "("}, {"IS_ALPHA": True, "OP": "+"}, {"ORTH": "et"}, {"ORTH": "al."}, {"ORTH": ", "},
                      {"IS_DIGIT": True}, {"ORTH": ")"}]]

    multi_citation_pattern = [[
        {"ORTH": "("},
        {"IS_ALPHA": True, "OP": "+"},
        {"ORTH": "&", "OP": "?"},
        {"IS_ALPHA": True, "OP": "*"},
        {"ORTH": ","},
        {"IS_DIGIT": True},
        {"ORTH": ";"},
        {"IS_ALPHA": True, "OP": "+"},
        {"ORTH": ","},
        {"IS_ALPHA": True, "OP": "*"},
        {"ORTH": "&", "OP": "?"},
        {"IS_ALPHA": True, "OP": "+"},
        {"ORTH": ","},
        {"IS_DIGIT": True},
        {"ORTH": ")"}
    ]]

    matcher.add("CITATION", single_author_pattern)
    matcher.add("CITATION", multiple_authors_pattern)
    matcher.add("CITATION", et_al_pattern)
    matcher.add("CITATION", multi_citation_pattern)

    def citation_component(doc):
        """Custom pipeline component to detect APA citations."""
        matches = matcher(doc)
        new_spans = [Span(doc, start, end, label="CITATION") for _, start, end in matches]

        # Filter out existing entities that overlap with citations
        filtered_ents = []
        for ent in doc.ents:
            if not any(span.start <= ent.start < span.end or span.start < ent.end <= span.end for span in new_spans):
                filtered_ents.append(ent)

        # Merge citations with the remaining entities
        doc.set_ents(filtered_ents + new_spans, default="unmodified")

        print(doc.ents)

        return doc

    return citation_component
