class TreeNode(object):
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def bst_insert(self, root, x):
        '''二叉排序树的插入方法'''
        node = TreeNode(x)
        if root is None:
            root = node 
        elif x < root.val:
            root.left = self.bst_insert(root.left,x)
        else:
            root.right = self.bst_insert(root.right,x)
        return root 
    def bst_delete(self, root, x):
        '''二叉查找树的删除方法
        root: root node
        x: target value
        q,p: precursor, current cursor '''

        # if leaf node: father to None
        # if one child: father to child
        # if 2 children: find direct decent(right child the most left) or vise versa
        p = root
        find = False
        while p and not find:
            if x == p.val:
                find = True
            elif x < p.val:
                q, p = p, p.left
            else:
                q, p = p, p.right
        if p is None:
            print(x,'Not found')
            return
        else:
            print(x,'Node found')

        # 查找主体
        if p.left is None and p.right is None:  # leaf node
            if p == root:
                root = None
            elif q.left == p:
                q.left = None
            else:
                q.right = None
        elif p.left is None or p.right is None:  # p has single branch 
            if p == root:
                if p.left is None:
                    root = p.right
                else:
                    root = p.left 
            else:
                if q.left == p and p.left:
                    q.left = p.left
                elif q.left == p and p.right:
                    q.left = p.right 
                elif q.right == p and p.left:
                    q.right = p.left
                else: 
                    q.right = p.right
        else:  # p has 2 children 
            t, s = p, p.left 
            while s.right:  # 查找p的前驱，即p左子树中最大的节点
                t,s = s, s.right 
            p.val = s.val   # 赋值
            if t == p:  # pay attention here 
                p.left = s.left 
            else: 
                t.right = s.left

    def bst_delete2(self, root, x):
        '''二叉树删除方法二，by ZionDeng'''
        # if x < root.val: find in left 
        # elif x > root.val: find in right 
        # else: root, find descent -> switch

        # 查找主体
        if x < root.val:
            root.left = self.bst_delete2(root.left, x)
        elif x > root.val:
            root.right = self.bst_delete2(root.right, x)
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
                    t,s = s, s.right 
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
        if node is None:
            return
        print(node.val, end=" ")
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)

    def inOrder_travel(self, node):
        if node is None:
            return
        self.inOrder_travel(node.left)
        print(node.val, end=" ")
        self.inOrder_travel(node.right)

    def postOrder_travel(self, node):
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
    ls_new = [3,5,2,4,1,6,9]
    for i in ls_new:
        tree.root = tree.bst_insert(tree.root,i)
    tree.breadth_travel()
    print(" < new list")
