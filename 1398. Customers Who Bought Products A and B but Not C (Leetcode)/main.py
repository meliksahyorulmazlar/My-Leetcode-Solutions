import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customer_dict = {}
    for index, row in customers.iterrows():
        customer_dict[row['customer_id']] = row['customer_name']

    dictionary = {}

    for index, row in orders.iterrows():
        name = row['product_name']
        customer = row['customer_id']
        if customer not in dictionary:
            dictionary[customer] = [name]
        else:
            dictionary[customer].append(name)

    ids = []
    names = []
    for key in dictionary:
        result = dictionary[key]
        if "A" in result and 'B' in result and 'C' not in result:
            ids.append(key)
            names.append(customer_dict[key])

    return pd.DataFrame({"customer_id": ids, "customer_name": names})

