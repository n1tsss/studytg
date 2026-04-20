from fastapi import APIRouter, Depends

from app.api.dependencies import verify_admin_token

router = APIRouter(prefix='/exports', tags=['exports'])


@router.get('/csv')
def export_csv(_: str = Depends(verify_admin_token)) -> dict[str, str]:
    return {'status': 'csv queued'}
