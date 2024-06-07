class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        output = []
        for item in nums1:
            if item in nums2 or item in nums3:
                output.append(item)

        for item in nums2:
            if item in nums1 or item in nums3:
                output.append(item)
        return list(set(output))