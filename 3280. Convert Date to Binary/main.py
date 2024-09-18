class Solution:
    def convertDateToBinary(self, date: str) -> str:
        numbers = date.split("-")
        numbers = [int(n) for n in numbers]
        output_list = []

        for n in numbers:
            binary_list = []

            while n > 0:
                remainder = n % 2
                binary_list.append(str(remainder))
                n = n // 2

            output_list.append("".join(binary_list[::-1]))

        return "-".join(output_list)
