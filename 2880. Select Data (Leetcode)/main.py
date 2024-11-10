import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    name = []
    age = []
    for index, row in students.iterrows():
        if row["student_id"] == 101:
            name.append(row['name'])
            age.append(row['age'])
            break

    return pd.DataFrame({"name": name, "age": age})