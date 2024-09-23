class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        for i in range(k):
            number = nums[-1]
            nums.pop()
            nums.insert(0, number)
