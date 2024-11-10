import pandas as pd


def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    score_list = []

    for index, row in scores.iterrows():
        score = row["assignment1"] + row["assignment2"] + row["assignment3"]
        score_list.append(score)

    return pd.DataFrame({"difference_in_score": [max(score_list) - min(score_list)]})