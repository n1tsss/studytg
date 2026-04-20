from app.domain.models.score import Score
from app.domain.rules.score_validation import validate_score


def normalize_scores(scores: list[Score]) -> list[Score]:
    for score in scores:
        if not validate_score(score.value):
            raise ValueError('Invalid score value')
    return scores
