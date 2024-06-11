import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    bonus = []

    for (index, row) in employees.iterrows():
        name = row["name"]
        first_letter = name[0]
        if int(row["employee_id"]) % 2 == 1 and first_letter != "M":
            ids.append(row["employee_id"])
            bonus.append(row["salary"])
        else:
            ids.append(row["employee_id"])
            bonus.append(0)

    new_ids = sorted(ids)
    new_bonuses = [bonus[ids.index(new)] for new in new_ids]

    return pd.DataFrame({"employee_id": new_ids, "bonus": new_bonuses})