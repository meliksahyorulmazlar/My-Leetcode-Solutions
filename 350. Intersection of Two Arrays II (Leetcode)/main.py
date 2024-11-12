class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}

        for num in nums1:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1

        for num in nums2:
            if num not in dict2:
                dict2[num] = 1
            else:
                dict2[num] += 1
        possible = []
        for num in nums1:
            if num in nums2:
                if num not in possible:
                    count1 = dict1[num]
                    count2 = dict2[num]
                    for i in range(min(count1, count2)):
                        possible.append(num)
        return possible


