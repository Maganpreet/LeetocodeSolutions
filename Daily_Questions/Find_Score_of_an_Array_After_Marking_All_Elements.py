"""

You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

"""

import heapq
from collections import deque

class Solution:
    def findScore(self, nums: list[int]) -> int:
        idxs = dict()
        for i in range(len(nums)):
            if nums[i] not in idxs:
                idxs[nums[i]] = deque()   
            idxs[nums[i]].append(i)
        
        heaper = [nums[i] for i in range(len(nums))]
        heapq.heapify(heaper)
        
        processed = set()
        score = 0
        while heaper and len(processed) != len(nums):
            val =  heapq.heappop(heaper)
            idx = idxs[val].popleft()
            while heaper and (val, idx) in processed:
                val =  heapq.heappop(heaper)
                idx = idxs[val].popleft()

            score += val
            processed.add((val, idx))
            if idx > 0:
                processed.add((nums[idx-1], idx-1))
            if idx < len(nums)-1:
                processed.add((nums[idx+1], idx+1))

        return score
    

sol = Solution()

inp = [
    [2,1,3,4,5,2],
    [2,3,5,1,3,2]
]

for i in inp:
    print(f"The score after applying the algo {i} : ", sol.findScore(i))
            
