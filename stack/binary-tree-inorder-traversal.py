# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.dfs(root, output)
        return output
    
    def dfs(self, node, output):
        if node is None:
            return
        
        self.dfs(node.left, output)
        output.append(node.val)
        self.dfs(node.right, output)