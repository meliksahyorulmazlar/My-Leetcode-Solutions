class Solution:
    def triangleType(self, nums: List[int]) -> str:       
        if len([item for item in nums if item == nums[0]]) == 3:
            return "equilateral"

        for i in range(len(nums)):
            item = nums[i]
            nums.pop(i)
            if sum(nums) <= item:
                return "none"
            else:
                nums.insert(i,item)

        for num in nums:
            if nums.count(num) ==2:
                return "isosceles"
        return "scalene"