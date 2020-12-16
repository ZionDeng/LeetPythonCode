# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：
# “对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
from binary_tree import *


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        # 三种情况：
        # 1. 一个在左一个在右，2. 走在左； 3. 都在右
        if root is None:
            return
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right


if __name__ == '__main__':
    s = Solution()
    tree = Tree()
    for i in [3, 5, 1, 6, 2, 8]:
        tree.add(i)
    print(s.lowestCommonAncestor(tree.root, tree.root.left,tree.root.right).val)
