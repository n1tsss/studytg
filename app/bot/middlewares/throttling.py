from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware


class ThrottlingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        return await handler(event, data)
