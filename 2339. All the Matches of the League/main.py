import pandas as pd


def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    df = teams
    teams = []

    for index, row in df.iterrows():
        teams.append(row["team_name"])

    homes = []
    aways = []
    for team in teams:
        for t in teams:
            if t != team:
                homes.append(team)
                aways.append(t)

    return pd.DataFrame({"home_team": homes, "away_team": aways})
