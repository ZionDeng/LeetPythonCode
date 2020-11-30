# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。

# Definition for a binary tree node.
from binary_tree import *

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True 
        elif root.val == 1:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    head = Tree()
    list  = [0]
    for i in list:
        head.add(i)
    print(s.isUnivalTree(head.root))