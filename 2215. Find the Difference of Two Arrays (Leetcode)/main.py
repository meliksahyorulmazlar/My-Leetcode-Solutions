class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output1 = []
        output2 = []

        c1 = nums1
        c2 = nums2

        for num in nums1:
            if num in c2:
                continue
            else:
                if num not in output1:
                    output1.append(num)

        for num in nums2:
            if num in c1:
                continue
            else:
                if num not in output2:
                    output2.append(num)
        return [output1, output2]
