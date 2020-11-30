#
# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1
# such that A[0] < A[1] < ... A[i-1] < A[i] > \
#                             A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain,
# return any i such that A[0] < A[1] < ... A[i-1] < A[i] >
# A[i+1] > ... > A[A.length - 1].
from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        index = 0
        while A:
            while A[1] < A[0]:
                index += 1
                A.pop(0)
            while A[1] > A[0]:
                index += 1
                A.pop(0)
            return index
        # return A.index(max(A))



if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray([0, 1, 0]))
