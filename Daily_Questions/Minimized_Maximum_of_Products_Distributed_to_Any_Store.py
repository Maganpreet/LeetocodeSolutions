class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        min_dist = max(quantities)
        l, r = 1, min_dist

        def canDistribute(k, n):
            j=0
            remaining = quantities[j]
            for i in range(n):
                if remaining <= k:
                    j+=1
                    if j == len(quantities):
                        return True
                    remaining = quantities[j]
                else:
                    remaining = remaining - k

            return False
        
        while l <= r:
            mid = l + (r-l) // 2
            if canDistribute(mid, n):
                print(mid)
                min_dist = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_dist


sol = Solution()

inp = [(6, [11,6]),(7, [15,10,10]),(1, [100000])]

for i in inp:
    n, items = i
    print(f"minmized maximum products distributed : ", sol.minimizedMaximum(n,items))
