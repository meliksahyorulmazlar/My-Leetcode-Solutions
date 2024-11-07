class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length= len(matrix)
        dictionary = {}
        for i in range(length):
            for j in range(length):
                number = (i*(length-1))+j + (i+1)
                dictionary[number] = matrix[i][j]
        new_matrix = []
        for i in range(length):
            number = i+1
            row = []
            for j in range(length):
                new_number = number + (j*length)
                new_number = dictionary[new_number]
                row.append(new_number)
            new_matrix.append(row[::-1])


        for i in range(length):
            for j in range(length):
                matrix[i][j] = new_matrix[i][j]






sol = Solution()
sol.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]])