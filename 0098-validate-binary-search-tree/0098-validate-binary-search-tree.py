# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, miv, mav):
            if not node:
                return True
            if node.val <= miv or node.val >= mav:
                return False
            return validate(node.left, miv, node.val) and validate(node.right, node.val, mav)
        
        return validate(root, float('-inf'), float('inf'))