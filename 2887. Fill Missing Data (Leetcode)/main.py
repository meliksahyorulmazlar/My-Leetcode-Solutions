import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    names = []
    quantities = []
    prices = []
    for (index,row) in products.iterrows():
        names.append(row["name"])
        prices.append(row["price"])
        if pd.isnull(row["quantity"]):
            quantities.append(0)
        else:
            quantities.append(row["quantity"])
    return pd.DataFrame({"name":names,"quantity":quantities,"price":prices})