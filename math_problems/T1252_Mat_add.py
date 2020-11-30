from typing import List
from numpy import zeros


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        data = zeros((n, m))
        for x, y in indices:
            data[x, :] += 1
            data[:, y] += 1
        return sum(data % 2 == 1)
        # result = 0
        # mat = [[0] * m, [0] * m]
        # for addArr in indices:
        #     for i, nums in enumerate(mat[addArr[0]]):
        #         mat[addArr[0]][i] += 1
        #     for i, nums in enumerate(mat):
        #         nums[addArr[1]] += 1
        #
        #     print(mat)
        #
        # # count the odd
        # for index in mat:
        #     for nums in index:
        #         if nums % 2 == 1:
        #             result += 1
        #
        # return result


s = Solution()
print(s.oddCells(2, 3, [[0, 1], [1, 1]]))
