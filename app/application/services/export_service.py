from pathlib import Path


def report_path(base_dir: str, filename: str) -> Path:
    return Path(base_dir) / filename
