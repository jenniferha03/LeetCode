# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currSum = 0
        return self.dfs(root, targetSum, currSum)

    # dfs returns True when currSum == targetSum
    def dfs(self, node, targetSum, currSum): # node = 7, 22, currS = 20
        if node is None:
            return False

        currSum += node.val
        if node.left is None and node.right is None:
            return currSum == targetSum 
        l = self.dfs(node.left, targetSum, currSum) 
        r = self.dfs(node.right, targetSum, currSum)
        return l or r
