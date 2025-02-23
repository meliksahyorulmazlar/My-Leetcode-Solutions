class Solution(object):
    def moveZeroes(self, nums):
        # My first solution
        # for num in nums:
        #     if num == 0:
        #         nums.remove(num)
        #         nums.append(0)
        # return nums

        #Efficient Solution- My new solution
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j,len(nums)):
            nums[i] = 0
