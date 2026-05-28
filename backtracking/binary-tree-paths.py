# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.DFS(root,"", paths)
        return paths
    
    def DFS(self, node, curPath, paths):
        if node is None:
                return

        if curPath == "":
            curPath += str(node.val)
        else:
            curPath += "->" + str(node.val)
        if node.left is None and node.right is None:
            paths.append(curPath)
        else:
            self.DFS(node.left, curPath, paths)
            self.DFS(node.right, curPath, paths)
