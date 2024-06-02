class Solution(object):
    def shuffle(self, nums, n):
        x = []
        y = []
        half = len(nums) / 2
        for i in range(len(nums)):
            if i > half - 1:
                y.append(nums[i])
            else:
                x.append(nums[i])

        output = []
        for i in range(len(x)):
            output.append(x[i])
            output.append(y[i])
        return output