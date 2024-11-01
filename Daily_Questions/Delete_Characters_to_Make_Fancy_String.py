class Solution:
    def makeFancyString(self, s: str) -> str:
        freq = {}
        new = ""
        new += s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == new[-1]:
                count += 1
            else:
                count = 1
            if count >= 3:
                continue
            new += s[i]

        return new


class SolutionCaller:
    s = Solution()
    json = [
        "leeetcode",
        "aaabaaaa",
        "aab"
    ]
    for i in range(len(json)):
        print('Fancy String: ', s.makeFancyString(json[i]))
