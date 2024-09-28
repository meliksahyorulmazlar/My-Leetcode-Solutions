class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        found = False
        city = paths[0][1]
        count = len(paths)
        while count <= len(paths):
            previous_city = city
            for path in paths:
                if path[0] == city:
                    city = path[1]
            if previous_city == city:
                return city





