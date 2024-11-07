import pandas as pd


def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}
    for index, row in employees.iterrows():
        department = row["dept"]
        tpl = (row["emp_id"], row["salary"])
        if department not in dictionary:
            dictionary[department] = [tpl]
        else:
            dictionary[department].append(tpl)

    final_dict = {}
    for department in dictionary:
        result = dictionary[department]
        values = sorted(set([n[1] for n in result]))
        if len(values) > 1:
            value = values[-2]
            for n in result:
                if n[1] == value:
                    final_dict[n[0]] = department
    ids = sorted(final_dict)
    departments = [final_dict[i] for i in ids]
    return pd.DataFrame({"emp_id": ids, "dept": departments})


