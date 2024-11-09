"""
You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.

"""


class Solution:
    def getMaximumXor(self, nums, maximumBit: int):
        N = len(nums)
        for i in range(1, N):
            nums[i] = nums[i] ^ nums[i-1]

        max_val = 2**maximumBit - 1

        ans = [0] * N
        for i in range(N):
            ans[N-1-i] = max_val ^ nums[i]

        return ans

class SolutionHelper:
    sol = Solution()
    JSON = [
            ([0,1,1,3],2),
            ([2,3,4,7],3),
            ([0,1,2,2,5,7],3)
        ]
    for j in JSON:
        arr, maximumBit = j[0], j[1]
        print(f"Array with list of k's for i-th index '{j}' : ", sol.getMaximumXor(arr, maximumBit))

