import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    names = []
    salaries = []
    for (index,row) in employees.iterrows():
        names.append(row["name"])
        salaries.append(row["salary"]*2)

    return pd.DataFrame({"name":names,"salary":salaries})    