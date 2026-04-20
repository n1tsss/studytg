from sqlalchemy.orm import Session

from app.infrastructure.db.models import UserORM


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_telegram_id(self, telegram_id: int) -> UserORM | None:
        return self.db.query(UserORM).filter(UserORM.telegram_id == telegram_id).one_or_none()
