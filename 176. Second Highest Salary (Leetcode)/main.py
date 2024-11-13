import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = []
    for index, row in employee.iterrows():
        salary = row['salary']
        if salary not in salaries:
            salaries.append(row['salary'])

    if len(salaries) <= 1:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    return pd.DataFrame({"SecondHighestSalary": [sorted(salaries)[-2]]})