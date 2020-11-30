from typing import List


class ListNode:
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next


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


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result=[]
        while head:
            result.append(head.val)
            head=head.next
        return result[::-1]


s = Solution()
print(s.reversePrint(listToNode([2, 3, 1])))
