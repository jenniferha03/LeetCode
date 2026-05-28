# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        level = 0
        self.dfs(root, output, level)
        return output

    def dfs(self, node, output, level): #node = 9, output = [[3]], level = 1
        if node is None:
            return

        if len(output) <= level: #check if level has its index in output
            output.append([])
        output[level].append(node.val)
        level += 1
        self.dfs(node.left, output, level)
        self.dfs(node.right, output, level)

    

    