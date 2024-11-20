class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return k
        S = len(s)
        freq = {}
        for i in range(S):
            if s[i] not in freq:
                freq[s[i]] = 0
            freq[s[i]] += 1

        if not ('a' in freq and freq['a'] >= k and 'c' in freq and freq['c'] >= k and 'b' in freq and freq['b'] >= k):
            return -1
        l = r = max_window = 0
        while r < S:
            freq[s[r]] -= 1
            if freq[s[r]] < k:
                max_window = max(max_window, r - l)
                while freq[s[r]] < k:
                    freq[s[l]] += 1
                    l += 1
            r += 1
        max_window = max(max_window, r - l)
        return S - max_window
    

class SolutionHelper:
    s = Solution()
    inp = [("aabaaaacaabc",2),("a", 1),("abbbccbba",2),("abcacbabbc",3),("abccbabbbac",3)]

    for string, k in inp:
        print(f"Amount of characters that can be taken from both sides in minimum amount of time {(string)}: ", s.takeCharacters(string, k))


