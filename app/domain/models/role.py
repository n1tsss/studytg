from dataclasses import dataclass


@dataclass(slots=True)
class RoleInfo:
    code: str
    title: str
