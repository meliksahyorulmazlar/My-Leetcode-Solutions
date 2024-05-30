class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        paritiess = []
        if len(nums) == 1:
            return True
        elif len(nums) == 2:
            if nums[0] %2 == nums[1] %2:
                return False
            else:
                return True
        else:
            for i in range(1,len(nums)-1):
                previous = nums[i-1] % 2
                current = nums[i] % 2
                later = nums[i+1] %2
                if previous == current or current == later:
                    return False
            return True