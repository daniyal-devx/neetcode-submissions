class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Check if current node is good
            good = 1 if node.val >= max_so_far else 0
            
            # Update max for children
            new_max = max(max_so_far, node.val)
            
            # Count good nodes in left and right subtrees
            left_good = dfs(node.left, new_max)
            right_good = dfs(node.right, new_max)
            
            return good + left_good + right_good
        
        return dfs(root, root.val)