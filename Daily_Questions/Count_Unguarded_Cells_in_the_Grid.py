class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        count = 0
        cells = {
            "UNSAFE":0,
            "SAFE":1,
            "GUARD":2,
            "WALL":3
        }
        mat = [[cells["UNSAFE"]]*n for i in range(m)]

        for row, col in guards:
            mat[row][col] = cells["GUARD"]
        for row, col in walls:
            mat[row][col] = cells["WALL"]

        for row, col in guards:
            r = row-1
            while r > -1:
                if mat[r][col] == cells["GUARD"] or mat[r][col] == cells["WALL"]:
                    break
                mat[r][col] = cells["SAFE"]
                r -= 1
            r = row+1
            while r < m:
                if mat[r][col] == cells["GUARD"] or mat[r][col] == cells["WALL"]:
                    break
                mat[r][col] = cells["SAFE"]
                r += 1

            c = col-1
            while c > -1:
                if mat[row][c] == cells["GUARD"] or mat[row][c] == cells["WALL"]:
                    break
                mat[row][c] = cells["SAFE"]
                c -= 1
            c = col+1
            while c < n:
                if mat[row][c] == cells["GUARD"] or mat[row][c] == cells["WALL"]:
                    break
                mat[row][c] = cells["SAFE"]
                c += 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    count += 1

        return count

"""

[
    [
        [2, 3, 0, 1, 0, 0], 
        [1, 2, 1, 1, 3, 0], 
        [1, 1, 3, 2, 1, 1], 
        [1, 1, 0, 1, 0, 0]]

        [[1, 2, 3, 3], 
        [3, 1, 2, 3], 
        [2, 2, 3, 0]]

"""

sol = Solution()

inp = [
    [4,
    6,
    [[0,0],[1,1],[2,3]],
    [[0,1],[2,2],[1,4]]]
    [3,
    3,
    [[1,1]],
    [[0,1],[1,0],[2,1],[1,2]]]
    [3,
    4,
    [[0,1],[1,2],[2,0],[2,1]],
    [[1,3],[0,3],[1,0],[2,2],[0,2]]]
]

for i in inp:
    m, n, guards, walls = i
    print(f"Number of unguarded cells : ", sol.countUnguarded(m, n, guards, walls))
