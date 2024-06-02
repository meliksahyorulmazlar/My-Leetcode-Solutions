class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        if len(arr) == 2:
            return True
        else:
            gradient = arr[1] - arr[0]
            for i in range(1,len(arr)-1):
                if (arr[i+1] - arr[i]) != gradient:
                    return False
            return True
