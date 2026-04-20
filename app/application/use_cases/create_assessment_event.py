from app.application.dto.schemas import CreateAssessmentEventDTO
from app.domain.enums.event_status import EventStatus
from app.domain.models.assessment_event import AssessmentEvent


def create_assessment_event(event_id: int, payload: CreateAssessmentEventDTO) -> AssessmentEvent:
    return AssessmentEvent(
        id=event_id,
        group_id=payload.group_id,
        teacher_id=payload.teacher_id,
        mode=payload.mode,
        status=EventStatus.DRAFT,
    )
