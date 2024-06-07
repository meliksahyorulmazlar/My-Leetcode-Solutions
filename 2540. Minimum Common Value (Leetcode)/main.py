class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        common = list(s1&s2)
        if len(common) == 0:
            return -1
        else:
            return min(common)