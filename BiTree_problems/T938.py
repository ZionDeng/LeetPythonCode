# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int):
        result = 0

        return result

    def sortedArrayToBST(self, nums: List[int]):
        # 递归（数组）：取中间值；左边=递归（左边）；右边=递归（右边）
        if len(nums) <= 0:
            return None
        mid = len(nums) // 2
        result = TreeNode(nums[mid])

        result.left = self.sortedArrayToBST(nums[0:mid])
        result.right = self.sortedArrayToBST(nums[mid + 1:])

        return result


s = Solution()
print(s.rangeSumBST(s.sortedArrayToBST([10, 5, 15, 3, 7, None, 18]),7,15))
