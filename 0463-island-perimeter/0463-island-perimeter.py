class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int: 
        r = len(grid)
        c = len(grid[0])
        land = 0
        n = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    land += 1
                    # check top neighbor
                    if i > 0 and grid[i-1][j] == 1:
                        n += 1
                    # check left neighbor
                    if j > 0 and grid[i][j-1] == 1:
                        n += 1
                        
        return (land * 4) - (n * 2)
