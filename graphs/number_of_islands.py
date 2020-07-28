from typing import List
class Solution:
    def sink_islands(self,grid,i,j,m,n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = "0"
        self.sink_islands(grid,i-1,j,m,n)
        self.sink_islands(grid,i+1,j,m,n)
        self.sink_islands(grid,i,j-1,m,n)
        self.sink_islands(grid,i,j+1,m,n)

    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    number_of_islands = number_of_islands + 1
                    self.sink_islands(grid,i,j,m,n)
        return number_of_islands

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution()
    print(sol.numIslands(grid=grid))

