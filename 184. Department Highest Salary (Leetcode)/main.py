import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}
    for index, row in employee.iterrows():
        dpt = row['departmentId']
        salary = row['salary']
        if dpt not in dictionary:
            dictionary[dpt] = salary
        else:
            if dictionary[dpt] < salary:
                dictionary[dpt] = salary
    departments = []
    names = []
    salaries = []
    for index, row in employee.iterrows():
        dpt = row['departmentId']
        salary = row['salary']
        max_wage = dictionary[dpt]
        if max_wage == salary:
            departments.append(dpt)
            names.append(row['name'])
            salaries.append(salary)

    types = {}
    for index, row in department.iterrows():
        types[row['id']] = row['name']

    for i in range(len(departments)):
        departments[i] = types[departments[i]]

    return pd.DataFrame({"Department": departments, 'Employee': names, 'Salary': salaries})


