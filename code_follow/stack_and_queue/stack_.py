class Stack(object):
    """栈"""

    def __init__(self):
        self.items = []
        # 选择列表的话就用尾部压入压出
        # 选择单链表则需要用头部（因为时间复杂度）


    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.peek())
    for i in range(3):
        s.push(i)
    print(s.is_empty())
    print(s.size())
    print(s.pop())
    print(s)