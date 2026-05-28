# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        def find_parents(node, parent_map):
            queue = [node]

            while queue:
                cur = queue.pop(0)
                if cur.left:
                    parent_map[cur.left] = cur
                    queue.append(cur.left)
                if cur.right:
                    parent_map[cur.right] = cur
                    queue.append(cur.right)
                
        # Construct child-parent mapping
        parent_map = dict() 
        find_parents(root, parent_map)

        queue = [(target, 0)]
        visited = set()
        visited.add(target)

        output = []

        while queue:
            node, distance = queue.pop(0)

            if distance == k:
                output.append(node.val)

            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append((node.left, distance+1))
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append((node.right, distance+1))
            if node in parent_map and parent_map[node] not in visited:
                visited.add(parent_map[node])
                queue.append((parent_map[node], distance+1)) 

        return output