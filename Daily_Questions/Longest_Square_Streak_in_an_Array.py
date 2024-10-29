class Solution:
    def longestSquareStreak(self, nums) -> int:
        nums.sort()
        mx_ans = -1
        for i in range(len(nums)):
            sq = nums[i]*nums[i]
            if sq > 10**5:
                continue
            mx_ans = max(mx_ans, self.binarySearch(nums, i, len(nums)-1, sq, -1))

        return mx_ans if mx_ans != 0 else -1

    def binarySearch(self, nums, l, r, target, ans):
        if l > r:
            return ans

        mid = (l + r) // 2

        if nums[mid] > target:
            return self.binarySearch(nums, l, mid-1, target, ans)
        elif nums[mid] < target:
            return self.binarySearch(nums, mid+1, r, target, ans)
        if target == nums[mid]:
            target *= target 
            
            if ans == -1:
                ans = 2
            else:
                ans += 1
            return self.binarySearch(nums, mid+1, len(nums)-1, target, ans)
        

class SolutionCaller:
    sol = Solution()
    json = [
        [4,3,6,16,8,2],
        [2,3,5,6,7],
        [2,4],
        [27,3,9,18,81],
        [81,2,4,16,3,9,6561],
        [2,3,4,6,8,16]
    ]
    for i in range(len(json)):
        print('The longest Subsequence will be : ', sol.longestSquareStreak(json[i]))

