class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dictionary = {}
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] +=1

        results = [value for (key,value) in dictionary.items()]
        r1 = results[0]
        for result in results:
            if result != r1:
                return False
        return True
