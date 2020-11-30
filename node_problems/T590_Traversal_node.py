from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        while root:

            if root.val == None:
                res = self.postorder(root.children) + res
                return res
            else:
                res.append(root.val)
                root = root.children

        return res


def listToNode(intList):
    tem_node = Node()
    node = tem_node
    for item in intList:
        # # 记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        # if not tem_node.val:
        #     tem_node.val = item
        #     node = tem_node
        # else:
        tem_node.children = Node(item)
        tem_node = tem_node.children
    return node.children


def nodeToList(node):
    res = []
    while node:
        res.append(node.val)
        node = node.children
    return res


node = listToNode([1, None, 2, 3, None, 6, 5])

print(nodeToList(node))
s = Solution()

print(s.postorder(node))
