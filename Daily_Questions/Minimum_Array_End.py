"""
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        setbitposX = [0]*64
        setbitposN = [0]*64

        n -= 1

        for i in range(64):
            setbitposX[i] = (x >> i) & 1
            setbitposN[i] = (n >> i) & 1


        posX, posN = 0, 0
        #print(setbitposX)
        while posX < 63:
            while setbitposX[posX] != 0 and posX < 63:
                posX += 1
            setbitposX[posX] = setbitposN[posN]
            #print(setbitposX)
            posX += 1
            posN += 1
        result = 0
        #print(setbitposX)
        for i in range(64):
            if setbitposX[i] == 1:
                result += pow(2,i)
        #print(result)
        return result
    
class SolutionHelper:
    sol = Solution()
    JSON = [
            (2,13),(2,3),(3,4),(2,7)
        ]
    for j in JSON:
        n, x = j[0], j[1]
        print(f"Min value of arr[n-1] and also arr[n-1] is biggest in the arr and AND of all ints is x'{j}' : ", sol.minEnd(n,x))



        
