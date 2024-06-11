import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    names = []
    ages = []
    for (index,row) in students.iterrows():
        if row["student_id"] == 101:
            names.append(row["name"])
            ages.append(row["age"])
    return pd.DataFrame({"name":names,"age":ages})