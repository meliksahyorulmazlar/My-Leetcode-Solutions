class Solution:
    def letterCombinations(self, digits: str) -> None:
        phone_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                      "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        list1 = []
        list2 = []
        if len(digits) == 0:
            return list2
        for i in range(0, 1):
            char = digits[0]
            new_items = phone_dict[char]
            for item in new_items:
                list1.append(item)

        for i in range(1, len(digits)):
            new_characters = phone_dict[digits[i]]
            for i in list1:
                for j in new_characters:
                    list2.append(f"{i}{j}")
            list3 = []
            list1 = list2
            list2 = list3
        return list1