class Solution:
    def minimumMountainRemovals(self, nums) -> int:
        size = len(nums)
        inc_seq = [1] * size
        dec_seq = [1] * size

        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc_seq[i] = max(inc_seq[i], inc_seq[j] + 1)

        
        for i in range(size - 1, -1, -1):
            for j in range(size - 1, i, -1):
                if nums[i] > nums[j]:
                    dec_seq[i] = max(dec_seq[i], dec_seq[j] + 1)

        min_removals = float("inf")
        for i in range(size):
            if inc_seq[i] > 1 and dec_seq[i] > 1:
                min_removals = min(min_removals, size - inc_seq[i] - dec_seq[i] + 1)

        return min_removals        


class SolutionCaller:
    sol = Solution()
    json = [
        [1,3,1],
        [2,1,1,5,6,2,3,1],
        [5,6,7,8,1,2,3]
    ]
    for i in range(len(json)):
        print('Minimum removals to make it a mountain array : ', sol.minimumMountainRemovals(json[i]))