import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    count = {}
    for (index, row) in actor_director.iterrows():
        pair = (row["actor_id"], row["director_id"])
        if pair not in count:
            count[pair] = 1
        else:
            count[pair] += 1

    id1 = []
    id2 = []
    for (key, value) in count.items():
        if value >= 3:
            id1.append(key[0])
            id2.append(key[1])
    return pd.DataFrame({"actor_id": id1, "director_id": id2})