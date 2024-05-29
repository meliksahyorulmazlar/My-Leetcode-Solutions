class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num+1):
            number = str(i)
            amount = 0
            for char in number:
                amount += int(char)
            if amount % 2 == 0:
                count += 1
        return count