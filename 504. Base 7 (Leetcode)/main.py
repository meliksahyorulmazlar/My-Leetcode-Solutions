class Solution(object):
    def convertToBase7(self, num):
        bits = []
        if num == 0:
            return "0"
        if num < 0:
            num = -num
            while num != 0:
                remainder = num %7
                num = num//7

                bits.append(str(remainder))
            bits.reverse()
            return "-" + "".join(bits)
        else:
            while num != 0:
                remainder = num % 7
                num = num // 7

                bits.append(str(remainder))
            bits.reverse()
            return "".join(bits)
