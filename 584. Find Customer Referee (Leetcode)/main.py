import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    names = []
    for (index,row) in customer.iterrows():
        if pd.isnull(row["referee_id"]) or row["referee_id"] != 2:
            names.append(row["name"])
    return pd.DataFrame({"name":names})