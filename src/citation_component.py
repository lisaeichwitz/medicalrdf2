from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Span


@Language.factory("citation_component")
def create_citation_component(nlp, name):
    matcher = Matcher(nlp.vocab)

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
        matches = matcher(doc)
        new_spans = [Span(doc, start, end, label="CITATION") for _, start, end in matches]

        filtered_ents = []
        for ent in doc.ents:
            if not any(span.start <= ent.start < span.end or span.start < ent.end <= span.end for span in new_spans):
                filtered_ents.append(ent)

        doc.set_ents(filtered_ents + new_spans, default="unmodified")

        return doc

    return citation_component
