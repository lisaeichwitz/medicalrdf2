from spacy.language import Language


@Language.factory("description_extractor")
def create_description_extractor(nlp, name):
    return DescriptionExtractor()


class DescriptionExtractor:

    def __init__(self):
        pass

    def __call__(self, doc):
        descriptions = []

        for ent in doc.ents:
            tokenIndex = ent.start
            if ent.label_ == "DISORDER" and doc[tokenIndex].dep_ in {"nsubj", "nsubjpass"}:
                head = ent.root.head

                if head.pos_ == "VERB" or head.pos_ == 'AUX':
                    desc_tokens = []

                    for child in head.children:
                        if child.dep_ in {"attr", "acomp", "prep", "xcomp", "pobj", "dobj"}:
                            desc_tokens.append(child.subtree)

                    if desc_tokens:
                        description = " ".join([token.text for subtree in desc_tokens for token in subtree])
                        descriptions.append((ent.text, f"{head} {description}"))

        doc._.disorder_descriptions = descriptions
        return doc
