from collections import deque

class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:

        idxQ = deque()
        res = [-1] * (len(nums) - k + 1)

        for i in range(len(nums)):
            if idxQ and i - k + 1 > idxQ[0]:
                idxQ.popleft()
            if idxQ and nums[i] != nums[i-1]+1:
                idxQ.clear()
            idxQ.append(i)
            #print(idxQ)

            if i >= k-1:
                #print(idxQ)
                if len(idxQ) == k:
                    res[i-k+1] = nums[idxQ[-1]]
                else:
                    res[i-k+1] = -1
                #print(res)

        return res
    
sol = Solution()

inp = [([1,2,3,4,3,2,5], 3), ([2,2,2,2,2], 4), ([3,2,3,2,3,2], 2)]
for i in inp:
    nums, k = i
    print(f"Max power of in k size arrays {nums, k} : ", sol.resultsArray(nums, k))
