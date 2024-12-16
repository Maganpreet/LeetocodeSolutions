"""

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

"""

import heapq
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:

        def _calculate_gain(passes, totalStudents):
            return (
                (passes + 1) / (totalStudents + 1) - (passes) / (totalStudents) 
            )
        max_heap = []

        for passes, totalStudents in classes:
            gain = _calculate_gain(passes, totalStudents) 
            heapq.heappush(
                max_heap,
                (-gain, passes, totalStudents)
            )

        for _ in range(extraStudents):
            current_gain, passes, students = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -1*_calculate_gain(passes + 1, students + 1),
                    passes + 1,
                    students + 1
                )
            )
        avg = 0
        while max_heap:
            _, passes, students = heapq.heappop(max_heap)
            avg += passes / students

        return avg / len(classes)
    

sol = Solution()
inp = [([[1,2],[3,5],[2,2]], 2), ([[2,4],[3,9],[4,5],[2,10]], 4)]

for classes, extraStudents in inp:
    print(f"The maximized pass ratio will be : ", sol.maxAverageRatio(classes=classes, extraStudents=extraStudents))