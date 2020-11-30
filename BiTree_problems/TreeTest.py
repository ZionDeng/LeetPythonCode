from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    # 递归（数组）：取中间值；左边=递归（左边）；右边=递归（右边）
    if len(nums) <= 0:
        return None
    mid = len(nums) // 2
    result = TreeNode(nums[mid])

    result.left = sortedArrayToBST(nums[0:mid])
    result.right = sortedArrayToBST(nums[mid + 1:])

    return result


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


printTree(sortedArrayToBST([5, 3, 0, 1, 0, 2, 0]))
