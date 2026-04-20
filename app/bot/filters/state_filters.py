from aiogram.filters import BaseFilter


class StatePrefixFilter(BaseFilter):
    def __init__(self, prefix: str):
        self.prefix = prefix

    async def __call__(self, _, state=None) -> bool:
        if not state:
            return False
        return str(state).startswith(self.prefix)
