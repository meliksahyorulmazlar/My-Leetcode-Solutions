import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    name = []
    salary = []
    bonus = []
    for (index, row) in employees.iterrows():
        name.append(row["name"])
        salary.append(row["salary"])
        bonus.append(2 * row["salary"])
    return pd.DataFrame({"name": name, "salary": salary, "bonus": bonus})
