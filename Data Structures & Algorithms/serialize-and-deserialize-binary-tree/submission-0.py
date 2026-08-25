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
        nodes=deque(data.split(','))
        def build():
            val=nodes.popleft()
            if val=="null":
                return None
            node=TreeNode(int(val))
            node.left=build()
            node.right=build()
            return node
        return build()

