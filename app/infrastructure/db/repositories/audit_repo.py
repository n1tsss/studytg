class AuditRepository:
    def record(self, actor_id: int, action: str) -> dict[str, int | str]:
        return {'actor_id': actor_id, 'action': action}
