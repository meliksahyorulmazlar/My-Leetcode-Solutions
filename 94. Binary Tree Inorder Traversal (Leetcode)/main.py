# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        self.result = []

        self.inorderTraversal1(root)
        return self.result

    def inorderTraversal1(self, root):
        if not root:
            return None

        self.inorderTraversal1(root.left)
        self.result.append(root.val)
        self.inorderTraversal1(root.right)
