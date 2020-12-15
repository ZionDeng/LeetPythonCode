class Node:
    def __init__(self, item):
        self.elem = item
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        """层次遍历/广度优先
        用队列实现← 先进先出"""
        node = Node(item)
        # bool([None]) = True → 先判断
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def preorder_travel(self, node):
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)

    def inOrder_travel(self, node):
        if node is None:
            return
        self.inOrder_travel(node.left)
        print(node.elem, end=" ")
        self.inOrder_travel(node.right)

    def postOrder_travel(self, node):
        if node is None:
            return
        self.postOrder_travel(node.left)
        self.postOrder_travel(node.right)
        print(node.elem, end=" ")


if __name__ == '__main__':
    tree = Tree()

    for i in range(10):
        tree.add(i)
    tree.breadth_travel()
    print(" < original order")
    tree.preorder_travel(tree.root)
    print(" < pre_order")
    tree.inOrder_travel(tree.root)
    print(" < in_order")
    tree.postOrder_travel(tree.root)
    print(" < post_order")
    # 先中后序的遍历方法是根据根的位置判断
    # 从遍历数列回推的时候也注意观察根的位置
