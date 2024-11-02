class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                if sentence[i-1] != sentence[i+1]:
                    return False

        return True if sentence[0] == sentence[-1] else False


class SolutionHelper:
    sol = Solution()
    strings = [
        "leetcode exercises sound delightful",
        "eetcode",
        "Leetcode is cool"
    ]

    for s in strings:
        print(f'String \"{s}\" is circular : ', sol.isCircularSentence(s))
