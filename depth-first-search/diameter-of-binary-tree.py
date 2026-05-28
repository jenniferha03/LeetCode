# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        # dfs returns the max depth of the node's sub-trees
        def dfs(node):
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.longest_path = max(l + r, self.longest_path) 
            return max(l, r) + 1
        
        dfs(root)
        return self.longest_path
