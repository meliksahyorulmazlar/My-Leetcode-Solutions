import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}

    for index,row in sales.iterrows():
        date = row["sale_date"]
        if date not in dictionary:
            dictionary[date] = row["sold_num"]
        else:
            dictionary[date] -= row["sold_num"]

    sales = []
    dif = []
    for key in dictionary:
        sales.append(key)
        dif.append(dictionary[key])

    return pd.DataFrame({"sale_date":sales,"diff":dif})