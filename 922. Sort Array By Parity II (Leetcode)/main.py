class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = []
        even = [n for n in nums if n %2 == 0]
        odd = [n for n in nums if n %2 == 1]
        for i in range(len(odd)):
            n1 = even[0]
            n2 = odd[0]
            result.append(n1)
            result.append(n2)
            even.pop(0)
            odd.pop(0)
        return result
