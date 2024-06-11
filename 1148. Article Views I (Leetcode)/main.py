import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = []
    for (index,row) in views.iterrows():
        if row["author_id"] == row["viewer_id"]:
            ids.append(row["author_id"])
    ids = sorted(list(set(ids)))
    return pd.DataFrame({"id":ids})