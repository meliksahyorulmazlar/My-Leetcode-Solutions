class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arrays = []
        for i in range(numRows):
            arrays.append([])
        down = True
        index = 0

        for char in s:
            arrays[index].append(char)


            if index == numRows-1:
                down = False

            if index == 0:
                down = True

            if down:
                index += 1
            else:
                index -= 1
        output_string  = ""
        for arr in arrays:
            output_string += "".join(arr)
        return output_string



sol = Solution()
sol.convert('PAYPALISHIRING',4)