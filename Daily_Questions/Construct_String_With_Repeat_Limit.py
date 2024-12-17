import heapq
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        count = Counter(s)

        max_heap = [(-ord(c), cnt) for c, cnt in count.items()]
        heapq.heapify(max_heap)

        res = []

        while max_heap:
            char, cnt = heapq.heappop(max_heap)
            char = chr(-char)
            limit_cnt = min(cnt, repeatLimit)
            res.append(char * limit_cnt)

            if cnt - limit_cnt > 0 and max_heap:
                nxt_char, nxt_cnt = heapq.heappop(max_heap)
                nxt_char = chr(-nxt_char)
                res.append(nxt_char)
                if nxt_cnt > 1:
                    heapq.heappush(max_heap, (-ord(nxt_char), nxt_cnt - 1))
                heapq.heappush(max_heap, (-ord(char), cnt - limit_cnt))

        return "".join(res)


sol = Solution()
inp = [("cczazcc", 3), ("aababab", 2)]

for string, repeatLimit in inp:
    print(f"Reconstructed string for the string {string} : ", sol.repeatLimitedString(string, repeatLimit))


                
        
