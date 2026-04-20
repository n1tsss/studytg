from app.domain.rules.aggregation import average


def test_average() -> None:
    assert average([10, 20, 30]) == 20
