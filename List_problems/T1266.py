from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):

            if i > 0:
                x = max(points[i][0] - points[i - 1][0],
                        points[i - 1][0] - points[i][0],
                        points[i][1] - points[i - 1][1],
                        points[i - 1][1] - points[i][1]
                        )
                result += x
        return result


solution = Solution()
print(solution.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
