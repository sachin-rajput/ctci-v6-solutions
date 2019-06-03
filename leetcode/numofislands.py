# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded by water and is 
# formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        numOfIslands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.BFS(grid, i, j)
                    numOfIslands += 1
        
        return numOfIslands


    def BFS(self, grid, init_row_index, init_col_index):
        
        queue = []
        queue.append((init_row_index, init_col_index))

        grid[init_row_index][init_col_index] = '0'

        while queue:
            s = queue.pop(0)
            row_index = s[0]
            col_index = s[1]

            directions = [(-1,0), (1, 0), (0, -1), (0, 1)]

            for d in directions:
                new_row_index =  row_index + d[0]
                new_col_index =  col_index + d[1]

                if self.isSafe(grid, new_row_index, new_col_index) and grid[new_row_index][new_col_index] == '1':
                    queue.append((new_row_index, new_col_index))
                    grid[new_row_index][new_col_index] = '0'
    
    def isSafe(self, grid, i, j):
        R = len(grid)
        C = len(grid[0])

        if i < 0 or j < 0 or i >= R or j >= C:
            return False
        return True


G = Solution()

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(G.numIslands(grid))
