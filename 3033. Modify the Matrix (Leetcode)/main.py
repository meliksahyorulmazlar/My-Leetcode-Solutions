class Solution(object):
    def modifiedMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == -1:
                    elements = [m[j] for m in matrix]
                    matrix[i][j] = max(elements)
        return matrix
