class Solution:
    def hIndex(self, citations: List[int]) -> int:
        dictionary = {}

        for i,num in enumerate(citations):
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        
        h_index = len(citations)
        for i in range(len(citations),0,-1):
            total = 0
            for key,value in dictionary.items():
                if key >= h_index:
                    total += value
            
            if total >=h_index:
                return h_index
            else:
                h_index -= 1
        return 0