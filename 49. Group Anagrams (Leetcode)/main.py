class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = {}
        for st in strs:
            result = []
            for char in st:
                result.append(ord(char))
            result = tuple(sorted(result))
            if result not in dictionary:
                dictionary[result] = [st]
            else:
                dictionary[result].append(st)

        print(dictionary)
        if strs == ['']:
            return [['']]
        else:
            output = []
            for key, value in dictionary.items():
                output.append(value)
            return output