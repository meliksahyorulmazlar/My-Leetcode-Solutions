class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        for i in range(length,-1,-1):
            if sum(1 for n in citations if n >= i) >= i:
                return i
