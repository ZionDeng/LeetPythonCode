
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

def height(root):
    
    if root is None: 
        return 0 
    h = 1 
    h += max(height(root.left),height(root.right)) 
    return h 

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
tree.print_height()





