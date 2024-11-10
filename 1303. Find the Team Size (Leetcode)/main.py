import pandas as pd


def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    dictionary1 = {}
    dictionary2 = {}

    for index, row in employee.iterrows():
        team = row["team_id"]
        dictionary1[row["employee_id"]] = team

        if team not in dictionary2:
            dictionary2[team] = 1
        else:
            dictionary2[team] += 1
    ids = []
    teams = []
    for index, row in employee.iterrows():
        ids.append(row["employee_id"])
        team = dictionary1[row["employee_id"]]
        teams.append(dictionary2[team])

    return pd.DataFrame({"employee_id": ids, "team_size": teams})








