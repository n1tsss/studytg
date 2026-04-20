from fastapi import APIRouter

router = APIRouter(prefix='/webhook', tags=['webhook'])


@router.post('/telegram')
async def telegram_webhook(payload: dict) -> dict[str, str]:
    _ = payload
    return {'result': 'accepted'}
