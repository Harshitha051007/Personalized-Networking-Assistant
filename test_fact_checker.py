from app.services import fact_checker


def test_fact_checker_returns_summary():
    summary = fact_checker.fact_check("Artificial Intelligence")

    # Should return a string
    assert isinstance(summary, str)

    # Summary should not be empty
    assert len(summary) > 10
    