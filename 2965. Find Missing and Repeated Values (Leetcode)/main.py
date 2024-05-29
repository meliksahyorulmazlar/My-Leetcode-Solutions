class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numbers = [i for i in range(1,pow(len(grid),2)+1)]
        grid = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i]))]
        repeated_item = None
        missing_item = None
        for number in numbers:
            if number not in grid:
                missing_item = number
            elif grid.count(number) == 2:
                repeated_item = number
        return [repeated_item,missing_item]

        
        
        