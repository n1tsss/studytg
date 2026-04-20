from enum import Enum


class ScoreMode(str, Enum):
    INDIVIDUAL = 'individual'
    AVERAGE_EQUAL = 'average_equal'
    AVERAGE_DELEGATED = 'average_delegated'
