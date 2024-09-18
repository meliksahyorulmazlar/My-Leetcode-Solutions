class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        items = set()
        for num in nums:
            if nums.count(num) == 2:
                items.add(num)

        return list(items)
