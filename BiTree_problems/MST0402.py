from binary_tree import Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        # 递归（数组）：取中间值；左边=递归（左边）；右边=递归（右边）
        
        if len(nums) <= 0:
            return None
        mid = len(nums) // 2
        result = TreeNode(nums[mid])

        result.left = self.sortedArrayToBST(nums[0:mid])
        result.right = self.sortedArrayToBST(nums[mid+1:])

        return result


if __name__ == "__main__":
    
    solution = Solution()

    head = solution.sortedArrayToBST([-10, 3, 0, 5, 9])
    tree = Tree()
    tree.root = head
    tree.breadth_travel()
