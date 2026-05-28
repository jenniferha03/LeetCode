# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)

# dfs return True when the left_node subtree is symmetric to the right_node 
# subtree, else return False
    def dfs(self, left_node, right_node):
        if left_node is None or right_node is None:
            return left_node == right_node

        if left_node.val == right_node.val:
            outer_path = self.dfs(left_node.left, right_node.right)
            inner_path = self.dfs(left_node.right, right_node.left)	
            return outer_path and inner_path
        return False
