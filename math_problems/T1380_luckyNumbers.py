from typing import List


# Given a m * n matrix of distinct numbers,
# return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that
# it is the minimum element in its row and maximum in its column.

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = []
        reverse = []
        n = len(matrix)
        m = len(matrix[0])
        for row in matrix:
            row_mins.append(min(row))
        for i in range(m):
            reverse.append([matrix[j][i] for j in range(n)])
        for colomn in reverse:
            if max(colomn) in row_mins:
                return [max(colomn)]
        return []

        # row_min = [min(i) for i in matrix]
        # col_min = [max(i) for i in zip(*matrix)]
        # return [i for i in row_min if i in col_min]


if __name__ == '__main__':
    s = Solution()
    print(s.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
