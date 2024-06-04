class Solution(object):
    def duplicateNumbersXOR(self, nums):
        dictionary = {}

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        numbers = []
        for key in dictionary:
            if dictionary[key] == 2:
                numbers.append(key)

        if len(numbers) == 0:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        else:
            total = numbers[0]
            for number in numbers[1:]:
                total ^= number
            return total

