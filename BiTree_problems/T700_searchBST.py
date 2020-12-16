# t node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the given value.
# Return the subtree rooted with that node.
#  If such node doesn't exist, you should return NULL.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int):
        if root is None:
            return
        else:
            if root.val == val:
                return root
            elif root.val > val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)


if __name__ == '__main__':
    root = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    root.left = node1
    node1.left = node3
    node1.right = node4
    s = Solution()
    print(s.searchBST(root, 2).val)
