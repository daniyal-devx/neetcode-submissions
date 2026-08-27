# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue=deque(data.split(','))
        def build():
            val=queue.popleft()
            if val=='null':
                return None
            root=TreeNode(val)
            root.left=build()
            root.right=build()
            return root
        return build()

