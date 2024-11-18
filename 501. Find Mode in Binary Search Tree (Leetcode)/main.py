# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.frequency = {}
        self.traverse(root)
        greatest = max(self.frequency.values())
        return [n for n in self.frequency if self.frequency[n] == greatest]

    def traverse(self, root):
        if not root:
            return

        if root.val in self.frequency:
            self.frequency[root.val] += 1
        else:
            self.frequency[root.val] = 1

        self.traverse(root.left)
        self.traverse(root.right)

