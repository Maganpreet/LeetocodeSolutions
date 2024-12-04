class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l = r = 0
        S2 = len(str2)
        S1 = len(str1)
        if S2 > S1:
            return False
        
        while l < S1:
            asci1 = 97 if ord(str1[l]) + 1 > 122 else ord(str1[l]) + 1
            asci2 = ord(str2[r])
            if asci1 == asci2 or str1[l] == str2[r]:
                r += 1
            if r == S2:
                return True
            
            l += 1

        return False
        

sol = Solution()
inp = [
    ("abc","ad"),("zc","ad"),("ab","d")
]

for s1, s2 in inp:
    print(f"Whether we can make a string to contain a certain subsequence : ", sol.canMakeSubsequence(s1, s2))

"""
  l
abc

 r
ad

 
zc

ad
"""


