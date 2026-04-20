from app.domain.enums.event_status import EventStatus
from app.domain.models.assessment_event import AssessmentEvent


def approve_distribution(event: AssessmentEvent) -> AssessmentEvent:
    event.status = EventStatus.APPROVED
    return event
