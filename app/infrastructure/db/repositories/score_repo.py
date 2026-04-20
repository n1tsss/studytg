class ScoreRepository:
    def bulk_save(self, rows: list[dict]) -> int:
        return len(rows)
