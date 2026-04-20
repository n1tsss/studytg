def validate_score(value: float, min_score: float = 0, max_score: float = 100) -> bool:
    return min_score <= value <= max_score
