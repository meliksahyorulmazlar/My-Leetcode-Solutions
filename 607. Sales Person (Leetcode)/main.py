import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_id = ""
    for (index,row) in company.iterrows():
        if row["name"] == "RED":
            red_id = row["com_id"]

    ids = []
    for (index,row) in orders.iterrows():
        if row["com_id"] == red_id:
            ids.append(row["sales_id"])

    names = []
    for (index,row) in sales_person.iterrows():
        if row["sales_id"] in ids:
            continue
        else:
            names.append(row["name"])
    return pd.DataFrame({"name":names})
