class Solution:
    def minimumSubarrayLength(self, nums, k: int) -> int:
        OR = 0
        l = 0
        minLen = float("inf")
        bitCount = [0] * 32
        for r in range(len(nums)):
            self._updateBitCount(nums[r], bitCount, 1)

            while l <= r and self._convertBitCountToNumber(bitCount) >= k:
                #print(l, r, self._convertBitCountToNumber(bitCount))
                minLen = min(minLen, r-l+1)
                self._updateBitCount(nums[l], bitCount, -1)
                l += 1

        return minLen if minLen != float("inf") else -1
        
    def _updateBitCount(self, n, bitCount, delta):
        for i in range(32):
            if n & (1 << i):
                bitCount[i] += delta
    
    def _convertBitCountToNumber(self, bitCount):
        result = 0
        for pos in range(32):
            if bitCount[pos]:
                result += pow(2,pos)

        return result
    
class SolutionHelper:
    sol = Solution()
    json = [
        ([1,2,3], 2),
        ([2,1,8], 10),
        ([1,2], 0),
        ([1,2,32,21], 55)
    ]
    for j in json:
        print(f"Size of shortest subarray with OR at least K : ",sol.minimumSubarrayLength(j[0], j[1]))
