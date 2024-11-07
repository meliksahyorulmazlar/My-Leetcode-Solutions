class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        array = sorted(nums)
        return [i for i in range(len(array)) if array[i] == target]
