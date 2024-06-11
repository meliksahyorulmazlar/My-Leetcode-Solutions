import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    count = {}
    for (index,row) in courses.iterrows():
        course = row["class"]
        if course not in count:
            count[course] = 1
        else:
            count[course] += 1
    classes = []
    for key,value in count.items():
        if value >= 5:
            classes.append(key)
    return pd.DataFrame({"class":classes})