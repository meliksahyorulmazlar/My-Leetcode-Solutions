class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        index = 0
        forward = True
        for i in range(k):
            if forward:
                index += 1
            else:
                index -= 1
            if index == 0:
                forward = True

            if index == n - 1:
                forward = False
        return index
