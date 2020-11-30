class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, x):
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = ListNode(x)

    def print_self(self, head):
        if not head:
            print("none")
        while head.next:
            print(head.val,end=" ")
            head = head.next
        print(head.val)



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head:
        #     return head
        # data = [head.val]
        # temp = head
        # while temp.next:
        #     data.append(temp.next.val)
        #     temp = temp.next
        # data.reverse()
        # result = ListNode(data.pop(0))
        # temp = result
        # for datum in data.copy():
        #     while temp.next:
        #         temp = temp.next
        #     temp.next = ListNode(datum)
        # return result

        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev



if __name__ == '__main__':
    s = Solution()
    node = ListNode(0)
    for i in range(1, 5):
        node.add(i)
    new_node = s.reverseList(node)
    node.print_self(new_node)
