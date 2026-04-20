from dataclasses import dataclass


@dataclass(slots=True)
class TrainingSeason:
    id: int
    title: str
    is_active: bool = True
