class Solution(object):
    def deleteGreatestValue(self, grid):
        total = 0
        while len(grid[0]) !=0:
            items = []
            for i in range(len(grid)):
                current = grid[i]
                greatest = max(grid[i])
                grid[i].remove(greatest)
                items.append(greatest)
            total += max(items)
        return total