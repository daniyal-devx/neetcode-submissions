# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        res=[]
        while queue:
            current_level=[]
            level_size=len(queue)
            for i in range(level_size):
                curr=queue.popleft()
                current_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(current_level)
        return res
        