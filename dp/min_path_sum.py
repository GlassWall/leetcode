from typing import List
import sys
class Solution:
    def min_path(self,grid,row,col):
        if row == 0 and col == 0:
            return grid[row][col]
        if row == 0:
            return grid[row][col]+self.min_path(grid, row, col-1)
        if col == 0:
            return grid[row][col]+ self.min_path(grid,row-1,col)
        if row<len(grid) and col<len(grid[0]):
            return grid[row][col] + min(self.min_path(grid,row-1,col), self.min_path(grid,row,col-1))
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == None or grid[0] == None:
            return sys.maxsize
        m = len(grid)
        n = len(grid[0])
        return self.min_path(grid,m-1,n-1)

if __name__ == "__main__":
    grid = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
    sol = Solution()
    print(sol.minPathSum(grid=grid))