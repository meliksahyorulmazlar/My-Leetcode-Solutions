class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        average_differences = []

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        index = 0
        length = len(nums)
        while index < length:
            average1 = int(nums[index]/(index+1))

            denominator = (length-(index+1))
            average2 = 0
            if denominator != 0:
                average2 = int((nums[length-1]-nums[index])/denominator)

            result = abs(average1-average2)
            average_differences.append(result)
            index +=1

        item =  min(average_differences)
        item_index = average_differences.index(item)
        return item_index





sol = Solution()
x = sol.minimumAverageDifference(nums=[2,5,3,9,5,3])
print(x)