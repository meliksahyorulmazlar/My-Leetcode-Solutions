import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered = []
    for (index, row) in orders.iterrows():
        ordered.append(row["customerId"])

    names = []
    for (index, row) in customers.iterrows():
        if row["id"] not in ordered:
            names.append(row["name"])
    print(names)
    return pd.DataFrame({"Customers": names})