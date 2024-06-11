import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    name = []
    population = []
    area = []
    for (index,row) in world.iterrows():
        if int(row["area"]) >= 3000000 or int(row["population"]) >= 25000000:
            name.append(row["name"])
            population.append(row["population"])
            area.append(row["area"])
    return pd.DataFrame({"name":name,"population":population,"area":area})