class Solution:
    def sumZero(self, n: int) -> list[int]:
        if n == 1:
            return [0]
        else:
            zero = []
            if n % 2 ==0:
                for i in range(1,(n//2)+1):
                    zero.append(i)
                    zero.append(-i)
            else:
                zero.append(0)
                for i in range(1,(n//2)+1):
                    zero.append(i)
                    zero.append(-i)
            return zero
        
