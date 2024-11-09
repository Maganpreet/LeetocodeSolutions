"""
The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

"""

class Solution:
    def largestCombination(self, candidates) -> int:
        ans = [0 for i in range(24)]

        for i in range(24):
            for n in candidates:
                if (n & (1 << i)) >= 1:
                    ans[i] += 1

        return max(ans)
    


class SolutionHelper:
    sol = Solution()
    JSON = [
        [1, 5, 3],
        [16,17,71,62,12,24,14],
        [8,8],
        [7]
    ]
    for j in JSON:
        print(f"Largest count of number with bitwise AND > 0 '{j}' : ", sol.largestCombination(j))

