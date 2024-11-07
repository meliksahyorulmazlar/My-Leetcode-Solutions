class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            count = nums.count(num)
            for i in range(count-1):
                nums.remove(num)