# from link_lesson.single_link import SingleLinkList


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class DoubleLinkList(object):
    """单项循环链表"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = self.__head

    def is_empty(self):
        return self.__head is None

    def length(self):
        # 建立游标，遍历节点
        cursor = self.__head
        if self.is_empty():
            return 0
        else:
            # count记录数量
            count = 1
            while cursor.next != self.__head:
                count += 1
                cursor = cursor.next
            return count

    def travel(self):
        cur = self.__head
        if not self.is_empty():
            while cur.next != self.__head:
                print(cur.item, end=" ")
                cur = cur.next
            print(cur.item, end=" ")

        print("")

    def append(self, item):
        """链表尾部添加，尾插法"""
        node = Node(item)
        # 特殊处理
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cursor = self.__head
            # 需要用next作为判断
            while cursor.next != self.__head:
                cursor = cursor.next
            cursor.next = node
            node.next = self.__head

    def add(self, item):
        """头插法"""
        # 这个方法好像不用判断空诶
        node = Node(item)
        cursor = self.__head
        node.next = self.__head
        self.__head = node
        while cursor.next != node.next:
            cursor = cursor.next
        cursor.next = self.__head

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
            node.next = cursor.next
            cursor.next = node

    def search(self, item):
        """查找节点是否存在"""
        cursor = self.__head
        while cursor != self.__head:
            if cursor.item == item:
                return True
            else:
                cursor = cursor.next
        if cursor.item == item:
            return True
        return False

    def remove(self, item):
        """删除所有指定元素"""
        cursor = self.__head
        # 先判断是不是头结点
        if cursor.next:
            if cursor.item == item:
                if cursor.next != self.__head:
                    self.__head = cursor.next
                    cursor =cursor.next
                else:
                    self.__head = None
                    return
            while cursor.next != self.__head:
                if cursor.next.item == item:
                    cursor.next = cursor.next.next
                cursor = cursor.next
            cursor.next = self.__head





if __name__ == "__main__":
    doubleLinkList = DoubleLinkList()
    doubleLinkList.append(1)
    doubleLinkList.travel()
    doubleLinkList.remove(1)
    doubleLinkList.append(2)
    doubleLinkList.add(8)
    doubleLinkList.append(3)
    doubleLinkList.travel()
    doubleLinkList.append(4)
    doubleLinkList.append(5)
    doubleLinkList.insert(3, 10)
    doubleLinkList.append(6)
    doubleLinkList.remove(8)
    doubleLinkList.remove(6)
    doubleLinkList.travel()



