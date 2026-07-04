from app.services import topic_generator


def test_topic_generation_returns_suggestions():
    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]

    suggestions = topic_generator.generate_topics(themes, interests)

    # Should return a list
    assert isinstance(suggestions, list)

    # Should not be empty
    assert len(suggestions) > 0

    # Every suggestion should be a string
    for suggestion in suggestions:
        assert isinstance(suggestion, str)
        