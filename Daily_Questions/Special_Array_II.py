class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res = [True]*len(queries)
        violating_indices = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                violating_indices.append(i)

        for j in range(len(queries)):
            start, end = queries[j]
            start += 1
            lo, hi = 0, len(violating_indices) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if violating_indices[mid] > end:
                    hi = mid - 1
                elif violating_indices[mid] < start:
                    lo = mid + 1
                else:
                    res[j] = False
                    break
        return res

sol = Solution()

inp = [ ([3,4,1,2,6], [[0,4]]), ([4,3,1,6], [[0,2],[2,3]]) ]

for nums, queries in inp:
    print(f"Result of whether special array exist in those subarrays: ", sol.isArraySpecial(nums, queries))
