from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(index)):
            res.insert(index[i],nums[i])
        return res


solution = Solution()
nums = [0,1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(solution.createTargetArray(nums, index))
