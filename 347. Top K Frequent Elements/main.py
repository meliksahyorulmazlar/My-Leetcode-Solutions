class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for n in nums:
            if n not in numbers:
                numbers[n] = 1
            else:
                numbers[n] += 1
        print(numbers)
        result = sorted(numbers.keys(), key=lambda x: -numbers[x])

        return result[0:k]

