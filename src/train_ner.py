import spacy
from spacy.training import Example


class CustomNERTrainer:
    """Trains a custom Named Entity Recognition (NER) model in SpaCy."""

    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)
        self.ner = self.nlp.get_pipe("ner")

    def add_labels(self, labels):
        """Add new entity labels to the NER model."""
        for label in labels:
            self.ner.add_label(label)

    def train(self, train_data, n_iter=20):
        """Train the NER model with new entities."""
        optimizer = self.nlp.resume_training()
        for _ in range(n_iter):
            for text, annotations in train_data:
                example = Example.from_dict(self.nlp.make_doc(text), annotations)
                self.nlp.update([example], drop=0.5, sgd=optimizer)

    def save_model(self, output_dir="../models/custom_ner"):
        """Save the trained model."""
        self.nlp.to_disk(output_dir)
        print(f"Model saved to {output_dir}")


if __name__ == "__main__":
    from train_data import TRAIN_DATA

    trainer = CustomNERTrainer()
    trainer.add_labels(["DISORDER", "SYMPTOM", "TREATMENT"])
    trainer.train(TRAIN_DATA)
    trainer.save_model()
