import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    genders = []
    salaries = []
    for (index,row) in salary.iterrows():
        gender = row["sex"]
        ids.append(row["id"])
        names.append(row["name"])
        salaries.append(row["salary"])
        if gender == "m":
            genders.append("f")
        else:
            genders.append("m")
    return pd.DataFrame({'id':ids,"name":names,"sex":genders,"salary":salaries})
