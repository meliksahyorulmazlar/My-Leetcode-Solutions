import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    sigma_sum = 0
    total = 0
    for index,row in orders.iterrows():
        order = row["order_occurrences"]
        count = row["item_count"]
        total += order
        sigma_sum += (order*count)
    return pd.DataFrame({"average_items_per_order":[round(sigma_sum/total,2)]})