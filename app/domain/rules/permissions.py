from app.domain.enums.roles import Role


def can_manage_training(role: Role) -> bool:
    return role == Role.ADMIN


def can_submit_scores(role: Role) -> bool:
    return role == Role.TEACHER
