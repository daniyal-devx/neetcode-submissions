# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map value to its index in inorder for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to track current position in preorder
        self.pre_idx = 0
        
        def build(in_start: int, in_end: int) -> Optional[TreeNode]:
            # Base case: no elements to process
            if in_start > in_end:
                return None
            
            # Current root is the next element in preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find root's position in inorder
            root_idx = inorder_map[root_val]
            
            # Build left and right subtrees
            root.left = build(in_start, root_idx - 1)
            root.right = build(root_idx + 1, in_end)
            
            return root
        
        return build(0, len(inorder) - 1)