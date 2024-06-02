class Solution(object):
    def kthDistinct(self, arr, k):
        arr = [item for item in arr if arr.count(item)<2]
        if len(arr) < k:
            return ""
        else:
            return arr[k-1]