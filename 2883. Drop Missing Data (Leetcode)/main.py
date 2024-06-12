import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    ages = []
    for (index,row) in students.iterrows():
        if pd.isnull(row["name"]):
            pass
        else:
            ids.append(row["student_id"])
            names.append(row["name"])
            ages.append(row["age"])
    return pd.DataFrame({"student_id":ids,"name":names,"age":ages})