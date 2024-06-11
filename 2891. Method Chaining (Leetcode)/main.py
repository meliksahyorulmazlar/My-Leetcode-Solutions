import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    names = []
    weights = []
    for (index,row) in animals.iterrows():
        if int(row["weight"]) > 100:
            names.append(row["name"])
            weights.append(row["weight"])
    new_weights = sorted(weights,reverse=True)
    new_names = [names[weights.index(weight)] for weight in new_weights]
    return pd.DataFrame({"name":new_names})