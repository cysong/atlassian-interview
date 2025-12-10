
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_closest_value(self, root: Optional[TreeNode], target: float) -> Optional[int]:
        if root is None:
            return None
        
        node = root
        min_distince = abs(root.val - target)
        answer = root.val
        while node is not None:
            distance = abs(node.val - target)
            if distance == 0:
                return node.val
            elif distance < min_distince:
                min_distince = distance
                answer = node.val
            elif distance == min_distince:
                answer = min(answer, node.val)

            if target < node.val:
                node = node.left
            else:
                node = node.right
            
        return answer