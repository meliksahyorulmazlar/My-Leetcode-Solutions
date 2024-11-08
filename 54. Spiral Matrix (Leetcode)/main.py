class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            output = []
            for item in matrix[0]:
                output.append(item)
            return output
        elif n == 1:
            output = []
            for item in matrix:
                output.append(item[0])
            return output

        else:
            for i in range(n):
                output.append(matrix[0][i])

            for i in range(1,m):
                output.append(matrix[i][-1])

            for i in range(n-2,-1,-1):
                output.append(matrix[-1][i])

            for i in range(m-2,0,-1):
                output.append(matrix[i][0])

        matrices = matrix[1:m-1]
        recursion_matrix = [m[1:n-1] for m in matrices]
        print(recursion_matrix)
        try:
            if len(recursion_matrix[0]) >= 1:
                new_item = self.spiralOrder(recursion_matrix)
                print(new_item)
                for item in new_item:
                    output.append(item)
        except IndexError:
            return output

        return output



