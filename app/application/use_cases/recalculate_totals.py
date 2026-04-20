from app.domain.rules.aggregation import average


def recalculate_totals(scores: list[float]) -> float:
    return average(scores)
