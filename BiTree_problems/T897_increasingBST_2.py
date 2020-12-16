# Given a binary search tree,
# rearrange the tree in in-order
# so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only 1 right child.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add(self, elem):
        node = TreeNode(elem)
        queue = [self]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


class Solution:
    def increasingBST(self, root: TreeNode):

        s = []
        dummy = TreeNode(0)
        p = dummy

        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                cur = s.pop()
                root = cur.right
                cur.left = None
                p.right = cur
                p = p.right
        return dummy.right

    def print_tree(self, tree):
        if tree is None:
            return
        print(tree.val, end=" ")
        self.print_tree(tree.left)
        self.print_tree(tree.right)


if __name__ == '__main__':
    s = Solution()
    input_list = [3, 6, 2, 4, None, 8]
    tree = TreeNode(5)
    for input in input_list:
        tree.add(input)
    s.print_tree(tree)
    print()
    new_tree = s.increasingBST(tree)
    s.print_tree(new_tree)
