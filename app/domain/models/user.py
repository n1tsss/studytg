from dataclasses import dataclass

from app.domain.enums.roles import Role


@dataclass(slots=True)
class User:
    id: int
    telegram_id: int
    full_name: str
    role: Role
