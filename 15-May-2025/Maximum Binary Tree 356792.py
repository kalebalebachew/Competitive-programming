# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mx = nums.index(max(nums))
        root = TreeNode(nums[mx])
        root.left = self.constructMaximumBinaryTree(nums[:mx])
        root.right = self.constructMaximumBinaryTree(nums[mx+1:])
        
        return root