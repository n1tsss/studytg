from app.domain.enums.roles import Role


def allow_export(role: Role) -> bool:
    return role == Role.ADMIN
