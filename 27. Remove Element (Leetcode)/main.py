class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for num in nums:
            if num == val:
                count += 1
        for i in range(count):
            nums.remove(val)
            nums.append(nums)
        return len(nums) - count
