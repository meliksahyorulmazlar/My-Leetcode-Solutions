class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        n = len(nums)//2
        for i in range(n):
            greatest = max(nums)
            smallest = min(nums)
            nums.remove(greatest)
            nums.remove(smallest)
            average = (greatest+smallest)/2
            averages.append(average)
        return min(averages)
