"""
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

"""

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new = []
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and spaces[j] == i:
                new.append(" ")
                j += 1
            new.append(s[i])

        return "".join(new)
    

sol = Solution()
inp = [("LeetcodeHelpsMeLearn",[8,13,15]), ("icodeinpython",[1,5,7,9]), ("spacing",[0,1,2,3,4,5,6])]

for s, spaces in inp:
    print(f"The O(1) solution to add space to a string : ", sol.addSpaces(s, spaces))
        
