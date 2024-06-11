import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = 0
    average = 0
    high =0
    for (index,row) in accounts.iterrows():
        amount = row["income"]
        if amount < 20000:
            low += 1
        elif amount >= 20000 and amount <= 50000:
            average += 1
        else:
            high += 1
    return pd.DataFrame({"category":["High Salary","Low Salary","Average Salary"],"accounts_count":[high,low,average]})
