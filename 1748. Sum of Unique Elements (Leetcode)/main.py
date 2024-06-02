class Solution(object):
    def sumOfUnique(self, nums):
        distinct = []
        not_distinct = []
        for num in nums:
            if num not in distinct and num not in not_distinct:
                distinct.append(num)
            elif num in distinct:
                distinct.remove(num)
                not_distinct.append(num)
        if len(distinct) == 0:
            return 0
        else:
            return sum(distinct)

