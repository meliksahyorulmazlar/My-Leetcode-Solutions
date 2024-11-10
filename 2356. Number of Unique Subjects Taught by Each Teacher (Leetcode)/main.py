import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}

    for index, row in teacher.iterrows():
        subject = row["subject_id"]
        t = row["teacher_id"]
        if t not in dictionary:
            dictionary[t] = [subject]
        else:
            if subject not in dictionary[t]:
                dictionary[t].append(subject)

    ids = []
    count = []
    for t in dictionary:
        ids.append(t)
        count.append(len(dictionary[t]))

    return pd.DataFrame({"teacher_id": ids, "cnt": count})