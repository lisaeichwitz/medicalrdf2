from spacy.language import Language


@Language.factory("disorder_extractor")
def create_disorder_extractor(nlp, name):
    return DisorderExtractor()


class DisorderExtractor:
    """Custom spaCy component to extract disorder descriptions using dependency parsing."""

    def __init__(self):
        pass

    def __call__(self, doc):
        descriptions = []

        for ent in doc.ents:
            if ent.label_ == "DISORDER":
                head = ent.root.head  # The syntactic head of the disorder entity

                # If the head is a verb, extract its complement or object
                if head.pos_ == "VERB" or head.pos_ == 'AUX':
                    desc_tokens = []

                    # Collect adjectives, noun phrases, and complements
                    for child in head.children:
                        if child.dep_ in {"attr", "acomp", "prep", "xcomp", "pobj", "dobj"}:
                            desc_tokens.append(child.subtree)

                    # Merge all extracted tokens into a description
                    if desc_tokens:
                        description = " ".join([token.text for subtree in desc_tokens for token in subtree])
                        descriptions.append((ent.text, description))

        doc._.disorder_descriptions = descriptions
        return doc
