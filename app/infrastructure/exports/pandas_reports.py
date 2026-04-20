import pandas as pd


def summarize_scores(data: list[dict]) -> pd.DataFrame:
    frame = pd.DataFrame(data)
    if frame.empty:
        return frame
    return frame.groupby('student_id', as_index=False)['value'].mean()
