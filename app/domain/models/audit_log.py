from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class AuditLog:
    id: int
    actor_id: int
    action: str
    created_at: datetime
