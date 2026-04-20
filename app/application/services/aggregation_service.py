from app.domain.rules.aggregation import average


def aggregate_student_total(values: list[float]) -> float:
    return average(values)
