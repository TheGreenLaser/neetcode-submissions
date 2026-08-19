# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.prelimSearch(root, 0)

    def prelimSearch(self, root: Optional[TreeNode], cd) -> int:
        if root.left == None and not root.right == None:
            return self.prelimSearch(root.right, cd + 1)

        if not root.left == None and root.right == None:
            return self.prelimSearch(root.left, cd + 1)

        if not root.left == None and not root.right == None:
            return self.dfs(root.left) + self.dfs(root.right)
        
        if root.left == None and root.right == None:
            return cd

        
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return max(self.dfs(root.left) + 1, self.dfs(root.right) + 1)