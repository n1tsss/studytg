import pandas as pd


def to_csv(data: list[dict], path: str) -> str:
    pd.DataFrame(data).to_csv(path, index=False)
    return path
