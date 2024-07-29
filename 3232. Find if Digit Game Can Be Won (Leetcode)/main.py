class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = 0
        double_digit = 0
        for num in nums:
            string = str(num)
            if len(string) == 2:
                double_digit += num
            else:
                single_digit += num

        if single_digit == double_digit:
            return False
        else:
            return True        