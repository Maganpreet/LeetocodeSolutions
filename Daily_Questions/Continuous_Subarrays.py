"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

"""


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        l = 0
        subarrays = 0
        freq = {}

        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            while max(freq) - min(freq) >= 3:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            subarrays += r - l + 1
            
        return subarrays
    

sol = Solution()

inp = [
    [5,4,2,4],
    [1,2,3]
]

for i in inp:
    print(f"The number of continuous subarrays for array {i} : ", sol.continuousSubarrays(i))
