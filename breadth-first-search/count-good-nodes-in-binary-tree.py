# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        max_node = root.val
        
        def dfs(node, max_node): #node = 5, good_notes = 4, max = 5
            nonlocal good_nodes
            if node is None:
                return
            
            if node.val >= max_node: #5 >= 4:
                max_node = node.val
                good_nodes += 1
                
            dfs(node.left, max_node)
            dfs(node.right, max_node)
        
        dfs(root, max_node)
        
        return good_nodes
