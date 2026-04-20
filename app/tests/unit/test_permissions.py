from app.domain.enums.roles import Role
from app.domain.rules.permissions import can_manage_training


def test_admin_can_manage_training() -> None:
    assert can_manage_training(Role.ADMIN)
