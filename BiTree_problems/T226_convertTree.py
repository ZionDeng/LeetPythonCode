# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTree(root):
    if not root:
        return
    print('Binary Tree:')
    printInOrder(root, 0, " ★ ", 10)


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    # 递归（数组）：取中间值；左边=递归（左边）；右边=递归（右边）
    if len(nums) <= 0:
        return None
    mid = len(nums) // 2
    result = TreeNode(nums[mid])

    result.left = sortedArrayToBST(nums[0:mid])
    result.right = sortedArrayToBST(nums[mid + 1:])

    return result


def printInOrder(root, height, preStr, length):
    if not root:
        return
    printInOrder(root.right, height + 1, ' ', length)
    string = preStr + str(root.val) + preStr
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string) - leftLen
    res = " " * leftLen + string + " " * rightLen
    print(" " * height * length + res)
    printInOrder(root.left, height + 1, ' ', length)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root


s = Solution()
tree = sortedArrayToBST([1,2,3,4,6,7,9])
printTree(tree)
printTree(s.invertTree(tree))
