class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]
        for i in range(n):
            left_sum = sum(nums[0:i + 1])
            right_sum = sum(nums[i:])
            print(left_sum, right_sum)
            if left_sum == right_sum:
                return i + 1
        return -1

