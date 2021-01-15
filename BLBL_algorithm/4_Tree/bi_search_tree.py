from binary_tree_new import TreeNode, Tree


def bst_insert(root, x):
    '''二叉排序树的插入方法'''
    node = TreeNode(x)
    if root is None:
        root = node
    elif x < root.val:
        root.left = bst_insert(root.left, x)
    else:
        root.right = bst_insert(root.right, x)
    return root


def bst_delete(root, x):
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
        
def bst_delete2(root, x):
    '''二叉树删除方法二，by ZionDeng'''
    # if x < root.val: find in left 
    # elif x > root.val: find in right 
    # else: root, find descent -> switch

    # 查找主体
    if x < root.val:
        root.left = bst_delete2(root.left, x)
    elif x > root.val:
        root.right = bst_delete2(root.right, x)
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


tree = Tree()
ls_new = [15, 5, 3, 12, 16, 20, 23, 13, 18, 10, 6, 7]
for i in ls_new:
    # tree.root = tree.bst_insert(tree.root,i)
    tree.root = bst_insert(tree.root, i)
tree.breadth_travel()
print(" < BST travel")
# tree.bst_delete(tree.root, 12)
tree.root = tree.bst_delete(tree.root, 12)
tree.breadth_travel()
print(" < BST travel after deleted")
