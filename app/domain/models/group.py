from dataclasses import dataclass


@dataclass(slots=True)
class Group:
    id: int
    title: str
    point_id: int
