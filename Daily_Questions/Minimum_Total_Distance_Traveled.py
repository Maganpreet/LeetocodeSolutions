class Solution:
    def minimumTotalDistance(self, robot, factory) -> int:
        factory.sort()
        robot.sort()
        factory_pos = []
        #flatening the array based on the limit of the factory
        for f in factory:
            for _ in range(f[1]):
                factory_pos.append(f[0])

        cache = [[-1] * len(robot) for i in range(len(factory_pos))]
        #print(cache)

        def minDistance(roboIdx, facIdx, factory_pos):
            if roboIdx == len(robot):
                return 0

            if facIdx == len(factory_pos):
                return float("inf")

            if cache[facIdx][roboIdx] != -1:
                return cache[facIdx][roboIdx]

            choose = abs(robot[roboIdx] - factory_pos[facIdx]) + minDistance(roboIdx+1, facIdx+1, factory_pos)
            skip = minDistance(roboIdx, facIdx+1, factory_pos)

            cache[facIdx][roboIdx] = min(choose, skip)
            return cache[facIdx][roboIdx]

        return minDistance(0, 0, factory_pos)


class SolutionCaller:
    sol = Solution()
    json = [
        [0,4,6],
        [[2,2],[6,2]],
        [1,-1],
        [[-2,1],[2,1]],
        [0,5,6],
        [[2,2],[6,2]],
        [0,4,6],
        [[2,3],[6,0]],
        [-5,-2,2,5,7],
        [[-3,2],[0,2],[4,2]]
    ]
    for i in range(0, len(json), 2):
        print('Minimum total distance travelled by the robots : ', sol.minimumTotalDistance(json[i], json[i+1]))


