# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# Nary-Tree input serialization
# is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Definition for a Node.
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child) + 1 for child in root.children)


if __name__ == '__main__':
    '''
    初始化一颗测试二叉树:
            A
        B   C   D
      EFG       HIJ
    '''
    root = Node('A')
    B = Node('B')
    root.add_child(B)
    root.add_child(Node('C'))
    D = Node('D')
    root.add_child(D)
    B.add_child(Node('E'))
    B.add_child(Node('F'))
    B.add_child(Node('G'))
    D.add_child(Node('H'))
    D.add_child(Node('I'))
    D.add_child(Node('J'))

    s = Solution()
    print(s.maxDepth(root))
