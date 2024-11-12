import pandas as pd


def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    hashtags = {}

    for index, row in tweets.iterrows():
        tweet = row['tweet']
        words = tweet.split(" ")

        for word in words:
            if word[0] == "#":
                hashtag = word
                if hashtag not in hashtags:
                    hashtags[hashtag] = 1
                else:
                    hashtags[hashtag] += 1

    result = dict(sorted(hashtags.items(), key=lambda x: (-x[1], -ord(x[0][1]))))
    hashtags = []
    count = []

    i = 0

    for key in result:
        if i < 3:
            hashtags.append(key)
            count.append(result[key])
            i += 1
        else:
            break

    return pd.DataFrame({"hashtag": hashtags, 'count': count})
