import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    conditions = []
    for (index, row) in patients.iterrows():
        types = row["conditions"].split()
        if "DIAB1" in row["conditions"] and "SADIAB100" not in row["conditions"]:
            ids.append(row["patient_id"])
            names.append(row["patient_name"])
            conditions.append(row["conditions"])

    return pd.DataFrame({"patient_id": ids, "patient_name": names, "conditions": conditions})
