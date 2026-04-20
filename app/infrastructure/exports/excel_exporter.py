import pandas as pd


def to_excel(data: list[dict], path: str) -> str:
    pd.DataFrame(data).to_excel(path, index=False)
    return path
