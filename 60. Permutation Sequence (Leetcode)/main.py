class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        total = factorial(n)
        array = [i for i in range(1,n+1)]
        divisor = total//n
        output = ""
        k -= 1
        while array:
            index = k//divisor
            digit = array.pop(index)
            output += f"{digit}"

            k = k % divisor
            n = n-1
            if array:
                divisor = factorial(n)//n

        return output

def factorial(n)->int:
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n-1)