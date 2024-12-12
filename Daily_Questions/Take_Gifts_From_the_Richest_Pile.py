import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        stfig = [-gift for gift in gifts]
        heapq.heapify(stfig)
        while k:
            val = -1* heapq.heappop(stfig)
            new_val = math.floor(math.sqrt(val))
            heapq.heappush(stfig, -1 * new_val)
            k -= 1

        return -1 * sum(stfig)



sol = Solution()
inp = [([25,64,9,4,100],4), ([1,1,1,1],4), ([54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,13,33,69,19,40,13,10,43,61,72], 7)]

for gifts, k in inp:
    print(f"Remaining gifts after taking the gifts: ", sol.pickGifts(gifts, k))