class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        number = 1
        while len(missing) < k:
            if number not in arr:
                missing.append(number)
            number += 1
        return number-1