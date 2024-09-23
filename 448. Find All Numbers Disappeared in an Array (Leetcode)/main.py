class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dictionary = {i: 0 for i in range(1, len(nums) + 1)}
        for num in nums:
            dictionary[num] += 1

        nums = [n for n in dictionary if dictionary[n] == 0]

        return nums
