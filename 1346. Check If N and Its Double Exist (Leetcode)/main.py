class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if i != j:
                    if arr[i] == 2 * arr[j]:
                        return True
        return False
