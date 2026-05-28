# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([root, 1]) 
        while q:
            element = q.popleft() # element = [9, 2]
            node = element[0]  # node = 9
            depth = element[1] # depth = 2

            if node is None:
                continue
            if node.left is None and node.right is None:
                return depth
            depth += 1 #depth = 2
            q.append([node.left, depth])
            q.append([node.right, depth])

        return 0

