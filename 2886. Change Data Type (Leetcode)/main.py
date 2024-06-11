import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    ages = []
    grades = []
    for (index,row) in students.iterrows():
        ids.append(row["student_id"])
        names.append(row["name"])
        ages.append(row["age"])
        grades.append(int(row["grade"]))
    return pd.DataFrame({"student_id":ids,"name":names,"age":ages,"grade":grades})