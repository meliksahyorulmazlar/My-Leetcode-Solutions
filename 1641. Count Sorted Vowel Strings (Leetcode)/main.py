class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return len(["a", "e", "i", "o", "u"])

        values = ["a","e","i","o","u"]
        possible = ["a","e","i","o","u"]
        dictionary = {"a":1,"e":2,"i":3,'o':4,"u":5}

        for i in range(n-1):
            new_output = []
            for value in values:
                for char in possible:
                    if dictionary[char] >= dictionary[value]:
                        new_output.append(f"{char}")

            values = new_output

        return len(values)

