class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in columns:
                        columns.append(j)

        for i in range(len(matrix)):
            if i in rows:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0

        for row in matrix:
            for col in columns:
                row[col] = 0
