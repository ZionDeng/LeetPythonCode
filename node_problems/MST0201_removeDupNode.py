# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, root, item):
        while root.next:
            root = root.next
        node = ListNode(item)
        root.next = node


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None:
            return
        index = [head.val]
        if head.next is None:
            return head
        temp = head
        while temp.next.next:
            if temp.next.val in index:
                temp.next = temp.next.next
            else:
                index.append(temp.next.val)
                temp = temp.next
        if temp.next.val in index:
            temp.next = None
        return head

    def print_node(self, node):
        while node:
            print(node.val, end=" ")
            node = node.next


if __name__ == '__main__':
    test = [1,1, 3]
    head = ListNode(1)
    for item in test:
        head.add(head, item)
    s = Solution()
    s.print_node(head)
    print("origin")
    new_node = s.removeDuplicateNodes(head)
    s.print_node(new_node)
