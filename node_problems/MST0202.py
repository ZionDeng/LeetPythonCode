class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next

        return slow.val


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
solution = Solution()

print(solution.kthToLast(head=node1, k=2))
