from dataclasses import dataclass


@dataclass(slots=True)
class StudentProfile:
    user_id: int
    group_id: int
    is_leader: bool = False
