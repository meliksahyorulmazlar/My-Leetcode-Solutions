class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        for n in arr:
            if n not in dictionary:
                dictionary[n] = 1
            elif n in dictionary:
                dictionary[n] += 1

        values = [dictionary[n] for n in dictionary]

        set_form = set(values)

        if len(values) == len(set_form):
            return True
        else:
            return False

