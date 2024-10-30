from collections import defaultdict

class Solution:
    def maxMoves(self, grid) -> int:

        max_move = 0
        ROW, COL = len(grid), len(grid[0])
        cache = defaultdict(set) #{-1 for i in range(ROW * COL)}

        def dfs(row, col):
            #print(grid[row][col],row,col)
            if (row < 0 or row > len(grid)-1) and col > len(grid[0]):
                return 0
            
            if (row, col) in cache:
                return cache[(row, col)]
            a = b = c = 0 
            if row - 1 >= 0 and col + 1 < len(grid[0]) and grid[row][col] < grid[row-1][col+1]:
                a = 1 + dfs(row-1, col+1)
            if col + 1 < len(grid[0]) and grid[row][col] < grid[row][col+1]:
                b = 1 + dfs(row, col+1)
            if row + 1 < len(grid) and col + 1 < len(grid[0]) and grid[row][col] < grid[row+1][col+1]:
                c = 1 + dfs(row+1, col+1)
            
            #print(grid[row][col])            
            #print(a,b,c)
            cache[(row, col)] = max(a, b, c)
            return cache[(row, col)]
    
        for i in range(len(grid)):
            max_move = max(max_move, dfs(i, 0))
            #print(cache)

        return max_move
    
class SolutionCaller:
    sol = Solution()
    json = [
        [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]],
        [[3,2,4],[2,1,9],[1,1,7]],
        [[4,4,6,5],[6,6,6,9],[7,7,7,9],[8,9,7,9],[9,8,7,10],[10,10,10,10]],
        [[2,625152,3,5],[625151,625152,9,3]],
        [[207,141,103,12],[148,187,211,88],[116,16,67,157],[210,93,137,120],[52,116,241,86],[58,213,3,292]],
        [[19,13,5,10,30,19,28],[17,9,2,26,9,24,3],[1,12,13,21,18,12,8],[17,10,13,15,19,30,6],[14,5,24,24,17,22,6]],
        [[27,134,137,68],[265,270,273,72],[217,41,165,61],[40,269,19,75],[143,152,15,260],[149,173,38,63],[184,151,26,258],[171,278,112,37],[142,191,269,244]],
        [[42,19,111,153,142],[22,110,26,286,295],[27,35,69,186,47],[105,192,297,207,286]]
    ]
    for i in range(len(json)):
        print('Max numbers of moves possible in a grid : ', sol.maxMoves(json[i]))

