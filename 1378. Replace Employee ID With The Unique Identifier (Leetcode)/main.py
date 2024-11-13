import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}

    for index, row in employee_uni.iterrows():
        dictionary[row['id']] = row['unique_id']

    unique_ids = []
    names = []
    for index, row in employees.iterrows():
        i = row['id']
        if i not in dictionary:
            unique_ids.append(None)
        else:
            unique_ids.append(dictionary[i])
        names.append(row['name'])

    return pd.DataFrame({"unique_id": unique_ids, 'name': names})