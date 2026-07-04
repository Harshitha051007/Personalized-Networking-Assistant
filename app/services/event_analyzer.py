from transformers import pipeline
from app.config import MODEL_NAMES

classifier = pipeline(
    "zero-shot-classification",
    model=MODEL_NAMES["event_analysis"]
)


def extract_event_themes(description: str, candidate_labels=None):
    if candidate_labels is None:
        candidate_labels = [
            "AI",
            "healthcare",
            "blockchain",
            "education",
            "sustainability",
            "networking",
            "cybersecurity",
            "cloud computing",
            "machine learning",
            "finance"
        ]

    result = classifier(description, candidate_labels)

    return result["labels"][:3] 