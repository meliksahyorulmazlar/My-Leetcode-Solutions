import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    ages = []
    for (index,row) in df1.iterrows():
        ids.append(row["student_id"])
        names.append(row["name"])
        ages.append(row["age"])

    for (index,row) in df2.iterrows():
        ids.append(row["student_id"])
        names.append(row["name"])
        ages.append(row["age"])

    return pd.DataFrame({"student_id":ids,"name":names,"age":ages})
