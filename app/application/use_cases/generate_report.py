from app.application.dto.schemas import ReportRequestDTO


def generate_report(payload: ReportRequestDTO) -> str:
    return f'report_{payload.season_id}.{payload.format}'
