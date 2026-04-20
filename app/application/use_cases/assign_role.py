from app.domain.enums.roles import Role
from app.domain.models.user import User


def assign_role(user: User, role: Role) -> User:
    user.role = role
    return user
