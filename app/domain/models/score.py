from dataclasses import dataclass


@dataclass(slots=True)
class Score:
    event_id: int
    student_id: int
    value: float
