from app.domain.rules.score_validation import validate_score


def test_score_validation() -> None:
    assert validate_score(75)
    assert not validate_score(110)
