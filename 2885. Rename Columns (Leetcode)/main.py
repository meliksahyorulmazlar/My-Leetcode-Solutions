import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    surnames = []
    ages = []
    for (index,row) in students.iterrows():
        ids.append(row["id"])
        names.append(row["first"])
        surnames.append(row["last"])
        ages.append(row["age"])
    return pd.DataFrame({"student_id":ids,"first_name":names,"last_name":surnames,"age_in_years":ages})
