class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False

