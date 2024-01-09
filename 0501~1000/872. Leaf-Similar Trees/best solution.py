# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        self.dfs(root1,stack1)
        self.dfs(root2,stack2)

        return stack1 == stack2
    

    def dfs(self,root,stack):
        if root is None:
            return None
        if root.left is None and root.right is None:
            stack.append(root.val)
        self.dfs(root.left,stack)
        self.dfs(root.right,stack)
