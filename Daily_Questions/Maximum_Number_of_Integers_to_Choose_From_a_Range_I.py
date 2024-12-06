class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        s = 0
        count = 0
        ban = set(banned)
        for i in range(1,n+1):
            if i in ban:
                continue
            s += i
            if s <= maxSum:
                count += 1
            else:
                break

        return count
    
sol = Solution()
inp = [ ([1,6,5], 5, 6), ([1,2,3,4,5,6,7], 8, 1), ([11], 7, 50) ]
for banned, n, maxSum in inp:
    print(f"max number to be chosen from the string that will meet the conditions : ", sol.maxCount(banned, n, maxSum))