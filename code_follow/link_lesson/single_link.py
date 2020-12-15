class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item   
        self.next = None
        


class SingleLinkList(object):
    # 注意每次要考虑特殊情况：头结点为空
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        # 建立游标，遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def append(self, item):
        """链表尾部添加，尾插法"""
        node = Node(item)
        # 特殊处理
        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head
            # 需要用next作为判断
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node

    def add(self, item):
        """头插法"""
        node = Node(item)
        # 注意★
        # node.next = self.__head
        # self.__head = node
        self.__head, node.next = node, self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos :from 0 to end;
        :param item:
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            temp = self.__head
            # for i in range(pos-1):
            #     temp = temp.next
            count = 0
            while count < (pos - 1):
                count += 1
                temp = temp.next
            node = Node(item)
            node.next = temp.next
            temp.next = node

    def search(self, item):
        """查找节点是否存在"""
        cursor = self.__head
        while cursor is not None:
            if cursor.item == item:
                return True
            else:
                cursor = cursor.next
        return False

    def remove(self, item):
        """删除所有指定元素"""
        cursor = self.__head
        # 先判断是不是头结点
        if cursor.item == item:
            self.__head = cursor.next
        else:
            while cursor.next is not None:
                if cursor.next.item == item:
                    cursor.next = cursor.next.next
                else:
                    cursor = cursor.next


if __name__ == "__main__":
    linkList = SingleLinkList()
    linkList.append(1)
    linkList.append(2)
    linkList.add(8)
    linkList.append(3)
    linkList.append(4)
    linkList.append(5)
    linkList.insert(10, 10)
    linkList.append(6)
    linkList.remove(10)
    linkList.travel()

    print("length", linkList.length())
    print("exist 10:", linkList.search(10))
