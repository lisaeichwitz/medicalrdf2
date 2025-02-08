from spacy.language import Language


class EntityRetokenizeComponent:
    def __init__(self, nlp):
        pass

    def __call__(self, doc):
        with doc.retokenize() as retokenizer:
            for ent in doc.ents:
                retokenizer.merge(doc[ent.start:ent.end], attrs={"LEMMA": str(doc[ent.start:ent.end])})
        return doc


@Language.factory("entity_retokenizer_component")
def create_entity_retokenizer_component(nlp, name):
    return EntityRetokenizeComponent(nlp)
