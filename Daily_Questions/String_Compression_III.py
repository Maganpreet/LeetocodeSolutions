class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1
        i = 0
        while i < len(word):
            # print(i)
            while i < len(word)-1 and word[i] == word[i+1]:
                i += 1
                count += 1

            if count > 9:
                comp += str('9'+ word[i]) * (count // 9)
                if count%9 != 0:
                    comp += str(count%9) + word[i]
            else:
                comp += str(count) + word[i]
            count = 1
            i += 1
        return comp

class SolutionHelper:
    sol = Solution()
    json = ["abcde",
    "aaaaaaaaaaaaaabb",
    "aaaaaaaaaaaaaabbbbbbbcccccaaa",
    "abcbdxyzzzzaaaa",
    "mmmmmmmmmmmmmmmmmmzzzzzzzzzzzzzzzzzzyyyyyyyyyyyfvs"
    ]
    for s in json:
        print(f"Compressed string of '{s}' : ", sol.compressedString(s))

