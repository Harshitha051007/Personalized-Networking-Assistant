from app.services import event_analyzer


def test_event_analysis_returns_labels():
    candidate_labels = [
        "AI",
        "healthcare",
        "blockchain",
        "education",
        "sustainability"
    ]

    result = event_analyzer.extract_event_themes(
        "AI in healthcare and diagnostics",
        candidate_labels
    )

    # Output should be a list
    assert isinstance(result, list)

    # Should return at least one theme
    assert len(result) > 0

    # Should return at most three themes
    assert len(result) <= 3

    # Every returned theme should come from the candidate labels
    for label in result:
        assert label in candidate_labels 