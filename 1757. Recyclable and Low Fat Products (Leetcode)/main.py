import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    ids = []
    for (index,row) in products.iterrows():
        if row["low_fats"] == "Y" and row["recyclable"] == "Y":
            ids.append(row['product_id'])
    return pd.DataFrame({"product_id":ids})