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


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    # 递归（数组）：取中间值；左边=递归（左边）；右边=递归（右边）
    if len(nums) <= 0:
        return None
    mid = len(nums) // 2
    result = TreeNode(nums[mid])

    result.left = sortedArrayToBST(nums[0:mid])
    result.right = sortedArrayToBST(nums[mid + 1:])

    return result


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        # if t1 and t2 :
        #     t1.val += t2.val
        #     t1.left = self.mergeTrees(t1.left, t2.left)
        #     t1.right = self.mergeTrees(t1.right, t2.right)
        #     return t1
        # return t1 or t2

        if  t1 and t2:
            result=TreeNode(t1.val+t2.val)
            result.left=self.mergeTrees(t1.left,t2.left)
            result.right=self.mergeTrees(t1.right,t2.right)
            return result
        return t1 or t2


s = Solution()
tree1 = sortedArrayToBST([5, 3, 1, 0, 2, 0])
# printTree(tree1)
tree2 = sortedArrayToBST([0, 2, 0, 3, 7])
tr = s.mergeTrees(tree1, tree2)
printTree(tr)
