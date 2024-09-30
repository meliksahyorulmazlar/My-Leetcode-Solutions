import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    player_dictionary = {}

    for index, row in activity.iterrows():
        player = row["player_id"]
        if player not in player_dictionary:
            player_dictionary[player] = row["event_date"]
        else:
            current_date = pd.Timestamp(player_dictionary[player])
            new_date = pd.Timestamp(row["event_date"])
            if new_date < current_date:
                player_dictionary[player] = row["event_date"]

    ids = []
    logins = []

    for d in player_dictionary:
        ids.append(d)
        logins.append(player_dictionary[d])

    return pd.DataFrame({"player_id": ids, "first_login": logins})
