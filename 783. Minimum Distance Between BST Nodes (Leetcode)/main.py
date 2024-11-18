# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.values = []

        self.traverse(root)

        output = []
        result = sorted(self.values)
        for i in range(1, len(result)):
            output.append(abs(result[i] - result[i - 1]))

        return min(output)

    def traverse(self, root):
        if not root:
            return

        self.values.append(root.val)

        self.traverse(root.left)
        self.traverse(root.right)