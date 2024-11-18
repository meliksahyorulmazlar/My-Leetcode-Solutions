# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        self.values = []

        self.traverse(root, target)
        result = sorted(self.values, key=lambda x: (abs(x), -x))

        return int(target - result[0])

    def traverse(self, node, value):
        if not node:
            return

        self.traverse(node.left, value)
        self.values.append(value - node.val)
        self.traverse(node.right, value)

