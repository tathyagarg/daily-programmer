# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, curr_sum: int = 0) -> bool:
        if not root: return False

        res = self.hasPathSum(root.left, targetSum, curr_sum + root.val)
        if res:
            return True

        res = self.hasPathSum(root.right, targetSum, curr_sum + root.val)
        if res:
            return True

        if not (root.left or root.right):
            return root.val + curr_sum == targetSum