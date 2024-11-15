# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        self.result = []
        self.preorderTraversal1(root)

        return self.result

    def preorderTraversal1(self, root):
        if not root:
            return None

        self.result.append(root.val)
        self.preorderTraversal1(root.left)
        self.preorderTraversal1(root.right)
