class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dictionary = {}

        for item in items1:
            if item[0] in dictionary:
                dictionary[item[0]] += item[1]
            else:
                dictionary[item[0]] = item[1]

        for item in items2:
            if item[0] in dictionary:
                dictionary[item[0]] += item[1]
            else:
                dictionary[item[0]] = item[1]

        keys = sorted(dictionary)
        result = []

        for key in keys:
            value = [key]
            value.append(dictionary[key])

            result.append(value)

        return result
