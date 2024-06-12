import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    ids = []
    for (index,row) in employees.iterrows():
        ids.append(row["employee_id"])
    for (index,row) in salaries.iterrows():
        ids.append(row["employee_id"])

    ids = sorted([item for item in ids if ids.count(item)== 1])
    return pd.DataFrame({"employee_id":ids})
