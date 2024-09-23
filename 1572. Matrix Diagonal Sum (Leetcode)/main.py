class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        values = set()
        for i in range(len(mat)):
            t1 = (i, 0 + i)
            values.add(t1)
            t2 = i, len(mat) - 1 - i
            values.add(t2)

        values = list(values)
        print(values)
        for value in values:
            total += mat[value[0]][value[1]]

        return total
