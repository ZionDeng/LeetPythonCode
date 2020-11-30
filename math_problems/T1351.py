from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0

        for i_list in grid:
            for item in i_list:
                if item < 0:
                    result+=1
        return result


solution = Solution()
print(solution.countNegatives([[1, -1], [-1, -1]]))
