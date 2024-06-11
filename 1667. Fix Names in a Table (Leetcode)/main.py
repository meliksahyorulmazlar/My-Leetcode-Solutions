import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    for (index,row) in users.iterrows():
        ids.append(row["user_id"])
        name = row["name"]
        name = name[0].upper() + name[1:].lower()
        names.append(name)

    new_ids = sorted(ids)
    new_names = [names[ids.index(item)] for item in new_ids]
    return pd.DataFrame({"user_id":new_ids,"name":new_names})