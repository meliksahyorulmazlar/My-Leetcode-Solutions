import pandas

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    ids = []
    ages = []
    for data in student_data:
        ids.append(data[0])
        ages.append(data[1])
    dictionary = {
        "student_id":ids,
        "age":ages
    }
    return pandas.DataFrame(dictionary)
