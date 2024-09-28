import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    values = []
    for (index,row) in customers.iterrows():
        if row["year"] == 2021 and row["revenue"] >0:
            values.append(row["customer_id"])

    return pd.DataFrame({"customer_id":values})
