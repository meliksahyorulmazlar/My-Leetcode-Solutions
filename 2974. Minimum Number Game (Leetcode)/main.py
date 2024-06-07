class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) != 0:
            s1 = min(nums)
            nums.remove(s1)
            s2 = min(nums)
            nums.remove(s2)
            arr.append(s2)
            arr.append(s1)
        return arr