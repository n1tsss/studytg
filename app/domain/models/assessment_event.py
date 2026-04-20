from dataclasses import dataclass

from app.domain.enums.event_status import EventStatus
from app.domain.enums.score_mode import ScoreMode


@dataclass(slots=True)
class AssessmentEvent:
    id: int
    group_id: int
    teacher_id: int
    mode: ScoreMode
    status: EventStatus
