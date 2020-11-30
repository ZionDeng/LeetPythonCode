from NodeTest import *
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p1, p2 = None, head
        for _ in range(m-1):
            p1, p2 = p2, p2.next
        start, end = p1, p2
        for _ in range(m-1, n):
            p1, p1.next, p2 = p2, p1, p2.next
        end.next = p2
        if start:
            start.next = p1
            return head
        return p1

head = listToNode([1,2,3,4,5])
res = Solution().reverseBetween(head,2,4)
print(nodeToList(res))