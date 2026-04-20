from app.domain.models.training import TrainingSeason


def create_training(season_id: int, title: str) -> TrainingSeason:
    return TrainingSeason(id=season_id, title=title)
