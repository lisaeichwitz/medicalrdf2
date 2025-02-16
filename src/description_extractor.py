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
        citations = []
        diagnoses = []

        for ent in doc.ents:
            if ent.label_ == "DISORDER":
                print(ent.text)
                sentence = ent.sent
                for entity in sentence.ents:
                    if (entity.label_ == "CITATION"):
                        print(entity.text)
                        citations.append((ent.text, entity.text))
        doc._.disorder_citations = citations

        for token in doc:
            if token.text == "diagnosis" and token.dep_ in {"nsubj", "nsubjpass"}:
                head = token.sent.root
                diagnosis_tokens = []

                for child in head.children:
                    if child.dep_ == "agent":
                        diagnosis_tokens.append(child.subtree)

                if diagnosis_tokens:
                    diagnosis = " ".join(
                        [t.text for subtree in diagnosis_tokens for t in subtree if not (t.ent_type_ == "CITATION")])
                    diagnoses.append((token.text, f"{head} {diagnosis}"))

        doc._.disorder_diagnoses = diagnoses

        for ent in doc.ents:
            tokenIndex = ent.start
            if ent.label_ == "DISORDER" and doc[tokenIndex].dep_ in {"nsubj", "nsubjpass"}:
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
                        descriptions.append((ent.text, f"{head} {description}"))

        doc._.disorder_descriptions = descriptions
        return doc
