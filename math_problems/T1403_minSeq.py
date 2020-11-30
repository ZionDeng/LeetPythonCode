from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            if sum(nums[:i]) >= sum(nums[i:]):
                return nums[i-1:]


if __name__ == '__main__':
    s = Solution()
    print(s.minSubsequence([6]))
