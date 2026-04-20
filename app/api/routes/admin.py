from fastapi import APIRouter, Depends

from app.api.dependencies import verify_admin_token

router = APIRouter(prefix='/admin', tags=['admin'])


@router.post('/training-season')
def create_training_season(_: str = Depends(verify_admin_token)) -> dict[str, str]:
    return {'status': 'created'}
