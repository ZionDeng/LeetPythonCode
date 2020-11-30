# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def listToNode(intList: List):
    tem_node = ListNode()
    node = ListNode()
    for i in intList:
        # 记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        if not tem_node.val:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = ListNode(i)
            tem_node = tem_node.next
    return node


def printNode(node):
    res = []
    while node:
        if node.next is None:
            res.append(node.val)
            print(res)
            return res
        else:
            res.append(node.val)
            node = node.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        pre = None
        if l1.val < l2.val:
            pre = l1
            pre.next = self.mergeTwoLists(l1.next, l2)
        else:
            pre = l2
            pre.next = self.mergeTwoLists(l1, l2.next)
        return pre
        # result = []
        #
        # while l2 is not None:
        #     while l1 is not None:
        #         if l2.val <= l1.val:
        #             result.append(l2.val)
        #             if l2.next is not None:
        #                 l2 = l2.next
        #         #     如果l2指向最后一个，那么就一直呆在那
        #         # 如果l2指向最后一个但是这个数是所有中最大的，那么无法执行这一句
        #
        #         result.append(l1.val)
        #         if l1.next is not None:
        #             l1 = l1.next
        #         elif l1.next is None and l1.val > l2.val:
        #             #             l1所有数都比l2当前数字小
        #             return listToNode(result)
        #         else:
        #             result.append(l2.val)
        #             return listToNode(result)
        #
        # return listToNode(result)


s = Solution()
l1 = listToNode([1,3,5])
l2 = listToNode([2,4,6])

printNode(s.mergeTwoLists(l1, l2))
