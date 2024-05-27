class Solution:
    def addBinary(self, a: str, b: str) :
        total = 0
        a_char = "".join(list(a)[::-1])
        b_char = "".join(list(b)[::-1])
        for i in range(len(a_char)):
            if a_char[i] == "1":
                total += pow(2,i)
        for i in range(len(b_char)):
            if b_char[i] == "1":
                total += pow(2,i)

        if total == 0:
            return "0"
        else:
            result = []
            while total >0:
                remainder = total % 2
                total = total //2

                result.append(str(remainder))
            number = "".join(result[::-1])
            return number
