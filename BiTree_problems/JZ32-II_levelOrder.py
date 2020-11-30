# 打印二叉树
from binary_tree import TreeNode, Tree
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root.root]
        result = []
        while queue:
            copy, queue = queue, []
            # 每次需要清空queue，用copy的数组来迭代获取节点
            line = []  # 用于获取每行的数字
            for node in copy:
                line.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(line)
        return result




if __name__ == "__main__":
    s = Solution()
    head = Tree()
    for x in [3, 9, 20, 15, 7]:
        head.add(x)
    print(s.levelOrder(head))
