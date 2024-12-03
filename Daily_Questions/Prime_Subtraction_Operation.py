"""
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

"""
import math

class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        def check_prime(num):
            i = 2
            print(int(math.sqrt(num)))
            while i < int(math.sqrt(num))+1:
                if num % i == 0:
                    return False
                i += 1
            return True
        bound = 0
        for i in range(len(nums)):
            if i != 0 and (nums[i] - nums[i-1]) <= 0:
                return False
            if i == 0:
                bound = nums[i]
            else:          
                bound = nums[i] - nums[i-1]          
            for p in range(bound-1, 1, -1):
                if check_prime(p):
                    nums[i] = nums[i] - p
                    break
        return True
    
sol = Solution()
inp = [[4,9,6,10], [6,8,11,12], [5,8,3]]
for i in inp:
    print(f"can this be made into prime {inp} : ", sol.primeSubOperation(i))
        

"""
[5,5,2]

[2]

"""    

