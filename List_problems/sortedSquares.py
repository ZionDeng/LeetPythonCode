# Given an array of integers A 
# sorted in non-decreasing order, 
# return an array of the squares of each number, 
# also in sorted non-decreasing order.
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i ** 2 for i in A)


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
