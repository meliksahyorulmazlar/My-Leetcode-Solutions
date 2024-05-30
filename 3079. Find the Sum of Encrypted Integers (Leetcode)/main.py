class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            numbers = [int(char) for char in list(str(num))]
            length = len(numbers)
            largest = str(max(numbers))
            total += int(largest*length)
        return total
        
    
