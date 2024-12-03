class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        ans = []
        price_beauty = {}
        max_beauty = 0
        items = sorted(items, key=lambda x:x[0])
        for i in range(len(items)):
            items[i][1] = max(max_beauty, items[i][1])
            max_beauty = max(max_beauty, items[i][1])

        for q in queries:
            ans.append(self.binary_search(items, q))        
        return ans
    
    def binary_search(self, items, q):
        l=0
        r=len(items)-1
        beauty = 0
        while l<=r:
            mid = l + (r-l) // 2
            if items[mid][0] <= q:
                beauty = items[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return beauty


"""
[[1,2],[1,3],[2,4],[3,2],[5,6]]
max = 6
{
    1:3
    2:4
    3:4
    5:6
}

"""

sol = Solution()
inp = [([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]), ([[1,2],[1,2],[1,3],[1,4]], [1]), ([[10,1000]], [5])]

for items, queries in inp:
    print(f"maximum beauty of an item whose price is less than or equal to all these {queries} : ", sol.maximumBeauty(items, queries))