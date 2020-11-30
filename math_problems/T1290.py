class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = 0
        while head:
            s = s * 2 + head.val
            head = head.next
        return s


solution = Solution()
node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)
node1.next = node2
node2.next = node3


print(solution.getDecimalValue(node1))
