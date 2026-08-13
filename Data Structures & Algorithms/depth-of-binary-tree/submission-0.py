# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            depth_left=0
            depth_right=0
            if not node:
                return 0
            elif not node.left and not node.right:
                return 1
            depth_left+=depth(node.left)
            depth_right+=depth(node.right)
            return 1 + max(depth_left,depth_right)
        max_depth=depth(root)
        return max_depth


        