class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # If this is a new level, create a new list
            if len(result) == level:
                result.append([])
            
            # Add current node to its level
            result[level].append(node.val)
            
            # Recurse to children with next level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result