from dataclasses import dataclass


@dataclass(slots=True)
class TrainingPoint:
    id: int
    title: str
