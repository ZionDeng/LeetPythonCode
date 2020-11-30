# Given an array of 2n integers,
# your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes
# sum of min(ai, bi) for all i from 1 to n as large as possible.
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums) - 1, 2):
            result += nums[i]

        # return result
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([1, 4, 3, 2]))
