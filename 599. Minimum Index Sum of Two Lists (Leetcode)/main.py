class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dictionary[list1[i]] = i+j

        least_index = min([value for (key,value) in dictionary.items()])
        output = []
        for (key,value) in dictionary.items():
            if dictionary[key] == least_index:
                output.append(key)
        return output
