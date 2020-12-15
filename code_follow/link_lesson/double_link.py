# from link_lesson.single_link import SingleLinkList


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""

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
            node.prev = cursor

    def add(self, item):
        """头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

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
            cursor = self.__head
            # for i in range(pos-1):
            #     temp = temp.next
            count = 0
            while count < (pos - 1):
                count += 1
                cursor = cursor.next
            node = Node(item)
            node.next = cursor
            node.prev = cursor.prev
            cursor.prev.next = node
            cursor.prev = node

    def search(self, item):
        """查找节点是否存在"""
        cursor = self.__head
        while cursor != None:
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
            # 判断链表是否只有一个节点
            if cursor.next:
                cursor.next.prev = None
        else:
            while cursor is not None:
                if cursor.item == item:
                    if cursor.next:
                        cursor.next.prev = cursor.prev
                    cursor.prev.next = cursor.next

                cursor = cursor.next


if __name__ == "__main__":
    doubleLinkList = DoubleLinkList()
    doubleLinkList.append(1)
    doubleLinkList.append(2)
    doubleLinkList.add(8)
    doubleLinkList.append(3)
    doubleLinkList.append(4)
    doubleLinkList.append(5)
    doubleLinkList.insert(10, 10)
    doubleLinkList.append(6)
    doubleLinkList.remove(1)
    doubleLinkList.travel()
