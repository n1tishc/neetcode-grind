# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # For every node, we get the left and right tree height, and compare ot with an 
        # already max value we have

        diameter = 0

        def dfs(node):

            nonlocal diameter

            if not node:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)

            diameter = max((left+right), diameter)

            return 1 + max(left, right)
        
        dfs(root)

        return diameter