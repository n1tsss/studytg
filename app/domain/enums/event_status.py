from enum import Enum


class EventStatus(str, Enum):
    DRAFT = 'draft'
    WAITING_DISTRIBUTION = 'waiting_distribution'
    APPROVED = 'approved'
