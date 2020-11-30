#
# Given a non-empty array of integers,
# every element appears twice except for one.
# Find that single one.
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            i = nums.pop(0)
            if i in nums:
                nums.remove(i)
            else:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,1,2,4]))
