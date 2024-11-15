# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        self.result = []
        self.postorderTraversal1(root)

        return self.result

    def postorderTraversal1(self, root):
        if not root:
            return None

        self.postorderTraversal1(root.left)
        self.postorderTraversal1(root.right)
        self.result.append(root.val)
