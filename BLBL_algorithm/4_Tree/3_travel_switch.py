# pre: GDAFEMHZ 
# IN: ADEFGHMZ 
# ->: POST: AEFDHZMG 
from binary_tree_new import TreeNode, Tree

def pre_in_2post(preOrder,inOrder):
    nLength = len(preOrder)
    if nLength <= 0:
        return None
    if nLength == 1:
        print(preOrder,end = ' ')
        return TreeNode(preOrder)
    root_item = preOrder[0]
    num = 0 
    while num < nLength:
        if inOrder[num] == root_item:
            break  # cut the string into root, left, right
        num += 1 
    # print('left is: ',preOrder[1:num+1],inOrder[:num])
    # print('right is: ',preOrder[num+1:],inOrder[num+1:])
    # print('root is: ', root_item)
    root = TreeNode(root_item)
    root.left = pre_in_2post(preOrder[1:num+1],inOrder[:num])
    root.right = pre_in_2post(preOrder[num+1:],inOrder[num+1:])
    print(root_item,end = ' ')

    return root 



PRE = 'GDAFEMHZ'
IN = 'ADEFGHMZ'
tree = Tree()
tree.root = pre_in_2post(PRE,IN)
print('< direct print')
tree.postOrder_travel(tree.root)
print('< print as a tree')