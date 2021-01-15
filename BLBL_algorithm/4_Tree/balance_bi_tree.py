
# 平衡二叉树： 二叉查找树，左右子树的高度差不能超过1 
# 否则进行节点旋转 → 平衡 
# 左左和右右对称 -> 单旋转
# 左右和右左对称 -> 双旋转
from binary_tree_new import TreeNode, Tree

def singleRotateLeft(root):
    '''平衡二叉树的单左旋转方法'''
    r0, r1 = root, root.left 
    r0.left, r1.right = r1.right, r0

    return r1

def singleRotateRight(root):
    '''平衡二叉树的单右旋转方法'''
    r0, r1 = root, root.right 
    r0.right, r1.left = r1.left, r0

    return r1

def doubleRotateLR(root):
    '''平衡二叉树，双旋转，左右'''
    root.left = singleRotateRight(root.left)
    root = singleRotateLeft(root)
    return root 

def doubleRotateRL(root):
    '''平衡二叉树，双旋转，右左'''
    root.right = singleRotateLeft(root.right)
    root = singleRotateRight(root)
    return root 


def height(root):
    '''获取节点的高度'''
    if root is None: 
        return 0 
    h = 1 
    h += max(height(root.left),height(root.right)) 
    return h 

def bbt_insert(root, x):
    '''
    method to insert x into balanced_binary_trees
    root: the root of the tree 
    x: the value that we want to insert 
    '''
    # # if None: root.val = x 
    # if root.val > x: 
    #     insert left
    #     if height(root.left) - height(root.right) == 2: 
    #         if x < root.left.val:
    #             singleRotateLeft(root)
    #         else:
    #             doubleRotateLR(root)
    # else: 
    if root is None:  
        node = TreeNode(x)
        return node 
    if x < root.val: 
        root.left = bbt_insert(root.left, x)  # 向左插入x 
        if height(root.left) - height(root.right) == 2:
            # 不平衡
            if x < root.left.val:  # 左左
                root = singleRotateLeft(root)
            else:  # 左右
                root = doubleRotateLR(root)
    else: 
        root.right = bbt_insert(root.right, x)  # 向右插入x
        if height(root.right) - height(root.left) == 2:
            if x > root.right.val:  # 右右
                root = singleRotateRight(root)
            else:  # 右左
                root = doubleRotateRL(root)
    return root 

    


ls1 = [6,3,1,2,4,7] 
tree = Tree()
for i in ls1:
    tree.root = tree.bst_insert(tree.root,i)
tree.breadth_travel()
print('left left')
print('height is: ',height(tree.root))
tree.singleRotateLeft()
tree.breadth_travel()
print('height is: ',height(tree.root))


ls1 = [2,1,4,3,7,5] 
tree = Tree()
for i in ls1:
    tree.root = tree.bst_insert(tree.root,i)
tree.breadth_travel()
print('<- right, right')
print('height is: ',height(tree.root))
tree.root = singleRotateRight(tree.root)
tree.breadth_travel()
print('height is: ',height(tree.root))


ls1 = [7,3,8,0,5,4,6] 
tree = Tree()
for i in ls1:
    tree.root = tree.bst_insert(tree.root,i)
tree.breadth_travel()
print('<- left, right ')
print('height is: ',height(tree.root))
tree.root = doubleRotateLR(tree.root)
tree.breadth_travel()
print('height is: ',height(tree.root))

ls1 = [2,1,5,4,3,6] 
tree = Tree()
for i in ls1:
    tree.root = tree.bst_insert(tree.root,i)
tree.breadth_travel()
print('<- right, left')
print('height is: ',height(tree.root))
tree.root = doubleRotateRL(tree.root)
tree.breadth_travel()
print('height is: ',height(tree.root))

print('bbt_insert test')
ls1 = [2,1,5,4,3,6] 
tree = Tree()
for i in ls1:
    tree.root = tree.bbt_insert(tree.root,i)
tree.breadth_travel()
print('height is: ',height(tree.root))





