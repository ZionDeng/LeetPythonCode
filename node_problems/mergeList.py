# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from NodeTest import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # res = ListNode(0)
        # node = res
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         node.next, l1 = l1, l1.next
        #     else:
        #         node.next, l2 = l2, l2.next
        #     node = node.next
        # if l1:
        #     node.next = l1
        # else:
        #     node.next = l2
        # return res.next

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


head1 = listToNode([1, 2, 4])
head2 = listToNode([1, 3, 4])
s = Solution()
res = s.mergeTwoLists(head1, head2)
print(nodeToList(res))
