class Solution:
    def decrypt(self, code, k: int):
        C = len(code)
        res = [0] * C
        l = 0
        cur_sum = 0
        for r in range(C + abs(k)):
            cur_sum += code[r % C]

            if r - l + 1 > abs(k):
                cur_sum -= code[l % C]
                l += 1

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l-1) % C] = cur_sum
                elif k < 0:
                    res[(r+1) % C] = cur_sum
                else:
                    return res 
        return res
    
class SolutionHelper:
    sol = Solution()
    inp = [([5,7,1,4], 3), ([1,2,3,4], 0), ([2,4,9,3], -2)]
    for code, k in inp:
        print(f"Decrypted code {code} : {sol.decrypt(code, k)}")

"""
 0 1 2 3 4 5 6 7
[5,7,1,4, , , , ], k = 3


-4 -3 -2 -1 0 1 2 3
[ ,  ,  ,  ,5,7,1,4] k = -3

"""
