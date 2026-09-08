# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True
        
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False

        return self.isBalanced(root.right) and self.isBalanced(root.left)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        answer1 = 1
        answer2 = 1

        if not root.left == None:
            answer1 = self.maxDepth(root.left) + 1

        if not root.right == None:
            answer2 = self.maxDepth(root.right) + 1

        return max(answer1, answer2)
        