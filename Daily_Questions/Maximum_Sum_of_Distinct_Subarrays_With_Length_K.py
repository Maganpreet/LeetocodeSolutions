class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        total = 0
        freq = dict()
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            if nums[r] in freq:
                freq[nums[r]] += 1
            else:
                freq[nums[r]] = 1
            if r - l + 1 > k:
                total -= nums[l]
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            #print(freq)
            if r - l + 1 == k and len(freq) == k:
                count = max(total, count)

        return count


sol = Solution()

inp = [([1,5,4,2,9,9,9], 3), ([4,4,4], 3), ([1,6,2,3,2,2,1,3], 3)]

for i in inp:
    nums, k = i
    print(f"Max subarray of length k of array {nums} : ", sol.maximumSubarraySum(nums, k))

"""

[1,5,4,2,9,9,9], k = 3

{
    1:1
    5:1
    4:1
}


"""     
