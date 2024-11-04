"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        
        new = s + s
        for i in range(len(new)):
            if new[i] == goal[0]:
                j = 0
                k = i
                while k < len(new) and j < len(goal) and new[k] == goal[j]:
                    k += 1
                    j += 1

                if j == len(goal):
                    return True

        return False
                
class SolutionHelper:
    sol = Solution()
    for tup in [("abcde", "cdeab"), ("abcde", "abced"), ("aa", "a")]:
        s, goal = tup
        print(f"Is the string '{s}' can become '{goal}' : ", sol.rotateString(s, goal))


"""
deabcdeabc
cdeab

"""
