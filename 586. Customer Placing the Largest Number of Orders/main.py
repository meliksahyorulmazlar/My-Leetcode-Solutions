import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}
    for index, row in orders.iterrows():
        number = row["customer_number"]
        if number not in dictionary:
            dictionary[number] = 1
        else:
            dictionary[number] += 1

    greatest_count = 0
    number = 0
    print(dictionary)
    for n in dictionary:
        if dictionary[n] > greatest_count:
            greatest_count = dictionary[n]
            number = n

    if number == 0:
        return pd.DataFrame({"customer_number": []})
    return pd.DataFrame({"customer_number": [number]})
