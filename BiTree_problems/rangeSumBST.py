# Given the root node of a binary search tree,
# return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.
# Definition for a binary tree node.



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add(self, item):
        node = TreeNode(item)
        queque = [self]
        while queque:
            cur_node = queque.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queque.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queque.append(cur_node.right)

    def preorder_travel(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        sum = 0
        if L <= root.val <= R:
            sum += root.val
        # sum += self.rangeSumBST(root.left, L, R)
        # sum += self.rangeSumBST(root.right, L, R)
        if root.val >= L:
            sum += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            sum += self.rangeSumBST(root.right, L, R)
        return sum


if __name__ == '__main__':
    array = [5, 15, 3, 7, 18]

    tree = TreeNode(10)

    for i in array:
        tree.add(i)

        
    # tree.preorder_travel(tree)
    s = Solution()
    print(s.rangeSumBST(tree, 7, 15))
