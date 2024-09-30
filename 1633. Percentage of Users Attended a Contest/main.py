import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total = 0
    for index, row in users.iterrows():
        total += 1

    contests = {}
    for index, row in register.iterrows():
        contest_id = row["contest_id"]
        if contest_id not in contests:
            contests[contest_id] = 1
        else:
            contests[contest_id] += 1

    for c in contests:
        if ((contests[c] / total) * 100) == int((contests[c] / total) * 100):
            contests[c] = ((contests[c] / total) * 100)
        else:
            x = (contests[c] / total) * 100
            x = round(x, 2)
            contests[c] = x

    contest_ids = sorted(contests, key=lambda x: (-contests[x], x))
    percentages = [contests[c] for c in contest_ids]

    return pd.DataFrame({"contest_id": contest_ids, "percentage": percentages})
