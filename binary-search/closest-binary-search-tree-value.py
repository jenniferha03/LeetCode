# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        return self.dfs(root, target)

    #dfs return the node value that is closest to the target
    def dfs(self, node, target): #node = 2, target = 6, parent = 2
        if node.left is None and node.right is None:
            return node.val

        tempTarget = node.val
        if target > node.val and node.right is not None:
            right = self.dfs(node.right, target)
            if abs(tempTarget - target) > abs(right - target):
                tempTarget = right

        if target < node.val and node.left is not None:
            left = self.dfs(node.left, target)
            if abs(tempTarget - target) >= abs(left - target):
                tempTarget = left
        return tempTarget