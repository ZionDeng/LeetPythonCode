from typing import List


class ListNode:
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next


def listToNode(intList: List):
    tem_node = ListNode()
    node = tem_node
    for item in intList:
        # # 记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        # if not tem_node.val:
        #     tem_node.val = item
        #     node = tem_node
        # else:
        tem_node.next = ListNode(item)
        tem_node = tem_node.next
    return node.next


def nodeToList(node):
    res = []
    while node:
        # if node.next is None:
        #     res.append(node.val)
        #     print(res)
        #     return res
        # else:
        res.append(node.val)
        node = node.next
    # print(res)
    return res


# head = listToNode([2, 3, None, 1, 2])
#
# print(nodeToList(head))
