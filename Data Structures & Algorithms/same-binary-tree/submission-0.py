# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p == q) and (p == None or q == None): return False
        if (p == q) and (p == None and q == None): return True
        if not p.val == q.val: return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)