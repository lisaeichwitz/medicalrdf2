from spacy.language import Language


@Language.factory("citation_extractor")
def create_citation_extractor(nlp, name):
    return CitationExtractor()


class CitationExtractor:

    def __init__(self):
        pass

    def __call__(self, doc):
        citations = []

        for ent in doc.ents:
            if ent.label_ == "DISORDER":
                sentence = ent.sent
                for entity in sentence.ents:
                    if entity.label_ == "CITATION":
                        citations.append((ent.text, entity.text))
        doc._.disorder_citations = citations
        return doc
