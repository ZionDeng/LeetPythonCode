from node_problems.NodeTest import *


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast_cursor = head
        slow_cursor = head
        while fast_cursor.next and fast_cursor.next.next:
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
        if fast_cursor.next:
            return slow_cursor.next
        else:
            return slow_cursor


if __name__ == '__main__':
    s = Solution()
    head = listToNode(list(range(6)))
    result = s.middleNode(head)
    print(nodeToList(result))
