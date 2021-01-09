from binary_tree_new import TreeNode, Tree 

def bst_insert(root, x):
    '''二叉排序树的插入方法'''
    node = TreeNode(x)
    if root is None:
        root = node 
    elif x < root.val:
        root.left = bst_insert(root.left,x)
    else:
        root.right = bst_insert(root.right,x)
    return root 



tree = Tree()
ls = list(range(10))
for i in ls:
    tree.add(i)
tree.breadth_travel()
print(" < original list")
tree = Tree()
ls_new = [3,5,2,4,1,6,9]
for i in ls_new:
    tree.root = bst_insert(tree.root,i)
tree.breadth_travel()
print(" < new list")
