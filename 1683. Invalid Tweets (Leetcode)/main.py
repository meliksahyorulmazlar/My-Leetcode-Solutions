import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ids = []
    for (index,row) in tweets.iterrows():
        if len(row["content"]) >= 16:
            ids.append(row["tweet_id"])
    return pd.DataFrame({"tweet_id":ids})