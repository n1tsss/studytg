from dataclasses import dataclass

from app.domain.enums.score_mode import ScoreMode


@dataclass(slots=True)
class CreateAssessmentEventDTO:
    group_id: int
    teacher_id: int
    mode: ScoreMode


@dataclass(slots=True)
class DistributionDTO:
    event_id: int
    values_by_student: dict[int, float]


@dataclass(slots=True)
class ReportRequestDTO:
    season_id: int
    format: str
