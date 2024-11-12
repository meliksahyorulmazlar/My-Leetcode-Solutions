import pandas as pd


def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ids = []
    for index, row in tweets.iterrows():
        identifier = row["tweet_id"]
        tweet = row["content"]
        if len(tweet) > 140:
            ids.append(identifier)
        elif tweet.count("#") > 3 or tweet.count("@") > 3:
            ids.append(identifier)

    return pd.DataFrame({"tweet_id": sorted(ids)})



