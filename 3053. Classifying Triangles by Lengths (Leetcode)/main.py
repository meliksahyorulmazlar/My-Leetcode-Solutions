import pandas as pd

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    results = []

    for index,row in triangles.iterrows():
        a = row['A']
        b = row['B']
        c = row['C']
        valid_triangle = True

        if a == b and b == c:
            results.append('Equilateral')
        elif a == b or b == c or a==c:
            sides = [a,b,c]
            total = sum(sides)

            for side in sides:
                if not(total-side > side):
                    valid_triangle = False

            if valid_triangle:
                results.append("Isosceles")
            else:
                results.append('Not A Triangle')
        else:
            sides = [a, b, c]
            total = sum(sides)
            for side in sides:
                if not(total-side >side) :
                    valid_triangle = False

            if valid_triangle:
                results.append("Scalene")
            else:
                results.append('Not A Triangle')

    return pd.DataFrame({"triangle_type":results})



