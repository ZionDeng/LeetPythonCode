# Given a binary search tree,
# rearrange the tree in in-order
# so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only 1 right child.

# FAIL
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # search into a list
        value_list = self.root2list(root)
        value_list.sort()
        print(value_list)
        # to tree
        result_tree = TreeNode(value_list.pop(0))
        temp = result_tree
        while value_list:
            tree = TreeNode(value_list.pop(0))
            while temp.right:
                temp = temp.right
            temp.right = tree
        return result_tree


    def root2list(self, tree: TreeNode):
        if tree is not None:
            result = [tree.val]
            result = result + self.root2list(tree.left) + self.root2list(tree.right)
            return result
        else:
            return []



    def print_tree(self, tree):
        if tree is not None:
            print(tree.val, self.print_tree(tree.left), self.print_tree(tree.right), end=" ")


if __name__ == '__main__':
    s = Solution()
    input_list = [5, 3, 6, 2]
    tree = TreeNode(4)
    for input in input_list:
        tree.add(input)
    s.print_tree(s.increasingBST(tree))
    print("finish")
