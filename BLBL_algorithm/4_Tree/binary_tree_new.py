'''
 # @ Author: Zion Deng
 # @ Create Time: 2021-01-08 22:51:49
 # @ Description: A class tool for Binary Trees
 '''

class TreeNode(object):
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class Tree(object):
    '''
    root: 根节点
    二叉树的插入删除方法
    树的广度加入方法
    树的广度遍历，前中后序遍历方法
    '''
    def __init__(self):
        self.root = None

    def bst_insert(self, root, x):
        '''二叉排序树的插入方法'''
        node = TreeNode(x)
        if root is None:
            root = node
        elif x < root.val:
            root.left = self.bst_insert(root.left, x)
        else:
            root.right = self.bst_insert(root.right, x)
        return root

    def bst_delete(self, root, x):
        '''二叉树删除方法二，by ZionDeng'''
        # if x < root.val: find in left
        # elif x > root.val: find in right
        # else: root, find descent -> switch

        # 查找主体
        if x < root.val:
            root.left = self.bst_delete(root.left, x)
        elif x > root.val:
            root.right = self.bst_delete(root.right, x)
        else:  # x is root
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:  # root has 2 children:
                t, s = root, root.left
                while s.right:  # 查找p的前驱，即p左子树中最大的节点
                    t, s = s, s.right
                root.val = s.val   # 赋值
                if t == root:  # pay attention here
                    root.left = s.left
                else:
                    t.right = s.left
            return root

        return root

    def add(self, item):
        """层次遍历/广度优先"""
        """用队列实现← 先进先出"""
        node = TreeNode(item)
        # bool([None]) = True → 先判断
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:  # 当queue里面有值时：
            cur_node = queue.pop(0)  # 拿出第一个节点，如果左空就放在左边，没空就放在queue里面
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

    def singleRotateLeft(self):
        '''平衡二叉树的单左旋转方法'''
        root = self.root 
        r0, r1 = root, root.left 
        r0.left, r1.right = r1.right, r0
        self.root = r1

        # return r1

    def print_height(self):
        '''打印树的高度'''
        def height(root):
            if root is None:
                return 0
            h = 1
            h += max(height(root.left), height(root.right))
            return h
        print(height(self.root))

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=" ")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def preorder_travel(self, node):
        '''前序遍历'''
        if node is None:
            return
        print(node.val, end=" ")
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)

    def inOrder_travel(self, node):
        '''中序遍历'''
        if node is None:
            return
        self.inOrder_travel(node.left)
        print(node.val, end=" ")
        self.inOrder_travel(node.right)

    def postOrder_travel(self, node):
        '''后序遍历'''
        if node is None:
            return
        self.postOrder_travel(node.left)
        self.postOrder_travel(node.right)
        print(node.val, end=" ")


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

    tree = Tree()
    ls_new = [3, 5, 2, 4, 1, 6, 9]
    for i in ls_new:
        tree.root = tree.bst_insert(tree.root, i)
    tree.breadth_travel()
    print(" < new list")
