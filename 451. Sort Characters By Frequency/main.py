class Solution:
    def frequencySort(self, s: str) -> str:
        dictionary = {}
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        result = sorted(dictionary.keys(), key=lambda x: -dictionary[x])
        output = ""
        for char in result:
            amount = dictionary[char]
            if amount > 1:
                for i in range(amount):
                    output += char
            else:
                output += char

        return output
