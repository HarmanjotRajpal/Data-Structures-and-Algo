grid = [[1,0,1],
        [1,0,0],
        [1,9,0]]
        
def dfs(row, col, m, n, grid, count):
    
    if row<0 or row>=m or col<0 or col>=n or grid[row][col]==0 or grid[row][col]==-1:
        return float("inf")
    
    if grid[row][col] ==9:
        return count
        

    temp = grid[row][col]
    grid[row][col] = -1
    
    v1 = dfs(row + 1, col, m, n, grid, count + 1)
    v2 = dfs(row - 1, col, m, n, grid, count + 1)
    v3 = dfs(row, col + 1, m, n, grid, count + 1)
    v4 = dfs(row, col - 1, m, n, grid, count + 1)
    
    grid[row][col] = temp
    
    return min(v1,v2,v3,v4)

m = len(grid) #row
n = len(grid[0])#col 


print(dfs(0, 0, m, n, grid, 0))
