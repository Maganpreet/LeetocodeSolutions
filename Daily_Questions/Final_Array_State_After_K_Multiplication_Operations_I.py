import heapq
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i], i))

        while k:
            min_elem, idx = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (min_elem * multiplier, idx))
            k -= 1

        res = [-1] * len(nums)
        while min_heap:
            min_elem, idx = heapq.heappop(min_heap)
            res[idx] = min_elem

        return res

sol = Solution()
inp = [([2,1,3,5,6], 5, 2), ([1,2], 3, 4)]

for arr, k, mul in inp:
    print(f"The final state of the array {arr} :  ", sol.getFinalState(arr, k, mul))