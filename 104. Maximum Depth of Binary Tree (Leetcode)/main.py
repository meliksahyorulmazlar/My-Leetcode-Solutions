# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.counts = []
        self.traverse(root, level=1)

        return max(self.counts)

    def traverse(self, root, level=1):
        if not root:
            self.counts.append(level - 1)
            return

        print(level)
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)

