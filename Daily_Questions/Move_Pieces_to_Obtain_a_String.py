"""

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l1 = l2 = 0
        S = len(start)
        T = len(target)
        while l1 < S or l2 < T:
            while l1 < S and start[l1] == '_':
                l1 += 1
            while l2 < T and target[l2] == '_':
                l2 += 1

            if l1 == S or l2 == T:
                return (l1 == S and l2 == T)
            if start[l1] != target[l2]:
                return False
            if start[l1] == 'L' and target[l2] == 'L' and l1 < l2:
                return False
            if start[l1] == 'R' and target[l2] == 'R' and l1 > l2:
                return False

            l1 += 1
            l2 += 1
        return True

        
sol = Solution()

inp = [("_L__R__R_", "L______RR"), ("R_L_", "__LR"), ("_R", "R_"), ("L_LR_", "L__LR"), ("_L__R__R_L", "L______RR_"), ("_L","LL")]

for src, target in inp:
    print(f"Whether it is possible to create target from src : ", sol.canChange(src, target))

            
