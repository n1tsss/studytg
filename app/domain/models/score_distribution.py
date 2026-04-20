from dataclasses import dataclass


@dataclass(slots=True)
class ScoreDistribution:
    event_id: int
    leader_id: int
    is_submitted: bool
