from dataclasses import dataclass


@dataclass(slots=True)
class TeacherProfile:
    user_id: int
    point_id: int
