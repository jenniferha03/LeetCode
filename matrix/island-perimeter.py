class Solution:
   def islandPerimeter(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                   return self.dfs(grid, row, col)
        return 0
   # dfs returns the perimeter of the island
   def dfs(self, grid, row, col): # row = 1, col = 1
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0:
            return 1

        perimeter = 0
        if grid[row][col] == 1: #pr = 1
            grid[row][col] = 2
            perimeter += self.dfs(grid, row - 1, col)
            perimeter += self.dfs(grid, row + 1, col)
            perimeter += self.dfs(grid, row, col - 1)
            perimeter += self.dfs(grid, row, col + 1)
        return perimeter