from aiogram.filters import BaseFilter


class RoleFilter(BaseFilter):
    def __init__(self, required_role: str):
        self.required_role = required_role

    async def __call__(self, _, user_role: str = 'student') -> bool:
        return user_role == self.required_role
