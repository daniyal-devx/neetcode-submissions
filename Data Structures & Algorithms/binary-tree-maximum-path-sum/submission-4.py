# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float('-inf')
        def maxpath(root):
            if not root:
                return 0
            left_max=max(0,maxpath(root.left))
            right_max=max(0,maxpath(root.right))
            current_path=root.val+left_max+right_max
            self.maxsum=max(self.maxsum,current_path)
            return root.val+max(left_max,right_max)
        maxpath(root)
        return int(self.maxsum)

        