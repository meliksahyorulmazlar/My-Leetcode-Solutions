import pandas as pd


def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    volumes = {}

    for index, row in products.iterrows():
        name = row["product_id"]
        volume = row["Width"] * row["Length"] * row["Height"]
        volumes[name] = volume

    houses = {}
    for index, row in warehouse.iterrows():
        amount = volumes[row["product_id"]] * row["units"]
        name = row["name"]
        if name not in houses:
            houses[name] = amount
        else:
            houses[name] += amount

    names = []
    v = []
    for house in houses:
        names.append(house)
        v.append(houses[house])

    return pd.DataFrame({"warehouse_name": names, "volume": v})

