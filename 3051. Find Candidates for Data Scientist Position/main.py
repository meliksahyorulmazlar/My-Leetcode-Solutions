import pandas as pd


def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    employees = {}
    ids = []
    for index, row in candidates.iterrows():
        candidate = row["candidate_id"]
        skill = row["skill"]
        if candidate in employees:
            employees[candidate].append(skill)
            if "Python" in employees[candidate] and "PostgreSQL" in employees[candidate] and "Tableau" in employees[
                candidate]:
                if candidate not in ids:
                    ids.append(candidate)
        else:
            employees[candidate] = [skill]

    ids = sorted(ids)

    return pd.DataFrame({"candidate_id": ids})
