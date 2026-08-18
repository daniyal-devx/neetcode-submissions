# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr=root
        new_node=TreeNode(val)
        if not root:
            return new_node
        while curr:
            if val<curr.val:
                if not curr.left:
                    curr.left=TreeNode(val)
                    return root
                else:
                    curr=curr.left
            elif val>curr.val:
                if not curr.right:
                    curr.right=TreeNode(val)
                    return root
                else:
                    curr=curr.right
        return root
        


        