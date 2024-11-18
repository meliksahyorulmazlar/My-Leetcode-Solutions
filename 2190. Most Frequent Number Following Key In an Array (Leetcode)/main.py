class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dictionary = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                number = nums[i + 1]
                if number not in dictionary:
                    dictionary[number] = 1
                else:
                    dictionary[number] += 1

        value = max(dictionary.values())

        for k in dictionary:
            if dictionary[k] == value:
                return k
