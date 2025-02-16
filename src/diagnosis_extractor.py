from spacy.language import Language


@Language.factory("diagnosis_extractor")
def create_diagnosis_extractor(nlp, name):
    return DiagnosisExtractor()


class DiagnosisExtractor:

    def __init__(self):
        pass

    def __call__(self, doc):
        diagnoses = []

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
        return doc
