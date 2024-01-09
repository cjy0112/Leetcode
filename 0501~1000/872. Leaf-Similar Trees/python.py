class Solution(object):
    def leafSimilar(self, root1, root2):
        def inorder(root, v):
            if root:
                inorder(root.left, v)
                if not root.left and not root.right:
                    v.append(root.val)
                inorder(root.right, v)
        
        v1, v2 = [], []
        inorder(root1, v1)
        inorder(root2, v2)
        return v1 == v2

# Use recursive to solve
