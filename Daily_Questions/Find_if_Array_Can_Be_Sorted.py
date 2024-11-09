"""
You are given a 0-indexed array of positive integers nums.

In one operation, you can swap any two adjacent elements if they have the same number of 
set bits
. You are allowed to do this operation any number of times (including zero).

Return true if you can sort the array, else return false.

"""


class Solution:
    def canSortArray(self, nums) -> bool:

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] <= nums[j]:
                    continue
                else:
                    if bin(nums[i]).count('1') == bin(nums[j]).count('1'):
                        nums[i], nums[j] = nums[j], nums[i]
                    else:
                        return False

        return True
    

class SolutionHelper:
    sol = Solution()
    JSON = [
        [8,4,2,30,15],
        [1,2,3,4,5],
        [3,16,8,4,2],
        [75,34,30],
        [177,29,256],
        [33,134,56,234],
        [174,175,234,188],
        [20,6,7,10,20,6,20]
    ]
    for j in JSON:
        print(f"Can the array be sorted '{j}' : ", sol.canSortArray(j))

