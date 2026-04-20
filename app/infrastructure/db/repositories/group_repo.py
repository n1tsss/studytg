class GroupRepository:
    def list_for_point(self, point_id: int) -> list[dict[str, int]]:
        return [{'point_id': point_id}]
