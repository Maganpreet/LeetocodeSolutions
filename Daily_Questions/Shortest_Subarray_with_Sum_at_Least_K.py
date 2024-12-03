from heapq import heappop, heappush

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:

        total = 0
        prefix_sum_heap = []
        shortest = float("inf")

        for i in range(len(nums)):
            total += nums[i]
            if total >= k:
                shortest = min(shortest, i+1)

            while (
                prefix_sum_heap and total - prefix_sum_heap[0][0] >= k
            ):
                num, idx = heappop(prefix_sum_heap)
                shortest = min(shortest, i-idx)
            heappush(prefix_sum_heap, (total, i))

        return -1 if shortest == float("inf") else shortest
    

sol = Solution()
inp = [([1], 1), ([1,2], 4), ([2,-1,2], 3), ([17,85,93,-45,-21], 150), ([84,-37,32,40,95], 167)]

for i in inp:
    nums, k = i
    print(f"Length of shortest subarray with sum at least k : ", sol.shortestSubarray(nums, k))
