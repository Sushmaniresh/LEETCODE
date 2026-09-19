class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        mins_passed = 0
        que = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2: 
                    que.append((r,c,0))
                elif grid[r][c]==1:
                    fresh_oranges +=1
        if fresh_oranges == 0:
            return 0 
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while que:
            r,c, mins = que.popleft()
            mins_passed = mins
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh_oranges-=1
                    que.append((nr,nc,mins+1))
        return mins_passed if fresh_oranges==0 else -1



        

                



        