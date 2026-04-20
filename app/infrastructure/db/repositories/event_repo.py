class EventRepository:
    def create(self, group_id: int, teacher_id: int, mode: str) -> dict[str, int | str]:
        return {'group_id': group_id, 'teacher_id': teacher_id, 'mode': mode}
