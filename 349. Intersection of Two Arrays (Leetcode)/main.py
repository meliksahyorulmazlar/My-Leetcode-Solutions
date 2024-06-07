class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        for item in nums1:
            if item in nums2:
                output.add(item)
        return list(output)