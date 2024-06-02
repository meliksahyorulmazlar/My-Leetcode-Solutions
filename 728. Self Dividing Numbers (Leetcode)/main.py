class Solution(object):
    def selfDividingNumbers(self, left, right):
        output = []
        for i in range(left,right+1):
            digits = [int(digit) for digit in list(str(i))]
            if 0 not in digits:
                if len(list(str(i))) == len([digit for digit in digits if i % digit == 0]):
                    output.append(i)
        return output
