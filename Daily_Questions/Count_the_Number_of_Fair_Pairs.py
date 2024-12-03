"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper

"""


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        def countFairPairsLessThanK(k):
            l, r = 0, len(nums)-1
            count = 0
            while l < r:
                if nums[l] + nums[r] < k:
                    count += r-l
                    l += 1
                else:
                    r -= 1
            return count
        print(countFairPairsLessThanK(upper+1))
        print(countFairPairsLessThanK(lower))
        return countFairPairsLessThanK(upper+1) - countFairPairsLessThanK(lower)
    

sol = Solution()
inp = [
    [[0,1,7,4,4,5], 3, 6],
    [[1,7,9,2,5], 11, 11],
    [[7,4,0,4,1,5], 3, 6]
]

for i in inp:
    nums, lower, upper = i
    print(f"Number of fair pairs : ", sol.countFairPairs(nums, lower, upper))