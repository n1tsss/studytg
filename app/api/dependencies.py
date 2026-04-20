from collections.abc import Generator

from fastapi import Header, HTTPException
from sqlalchemy.orm import Session

from app.config import get_settings
from app.infrastructure.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_admin_token(x_admin_token: str = Header(default='')) -> str:
    token = get_settings().admin_api_token
    if x_admin_token != token:
        raise HTTPException(status_code=401, detail='Invalid admin token')
    return x_admin_token
