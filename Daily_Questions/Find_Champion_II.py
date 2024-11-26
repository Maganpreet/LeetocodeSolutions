class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:

        inward_edge = {}

        for stronger, weaker in edges:
            if weaker not in inward_edge:
                inward_edge[weaker] = []
            inward_edge[weaker].append(stronger)
        
        if len(inward_edge) + 1 == n:
            for i in range(n):
                if i not in inward_edge:
                    return i
        else:
            return -1
        
class SolutionHelper:
    sol: Solution = Solution()
    inp = [(3,[[0,1],[1,2]]),(4,[[0,2],[1,3],[1,2]])]

    for n, edges in inp:
        print(f"The champion of the tournament is : ", sol.findChampion(n, edges))

