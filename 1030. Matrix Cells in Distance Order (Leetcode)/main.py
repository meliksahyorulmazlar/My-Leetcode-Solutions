class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        output = []
        for i in range(rows):
            for j in range(cols):
                new_list = [i,j]
                output.append(new_list)
        return sorted(output,key=lambda x:(abs(x[0]-rCenter)+abs(x[1]-cCenter)))