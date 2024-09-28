"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""


class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        values = []
        values.append(root.val)

        node = root.next
        while node is not None:
            print(values)
            values.append(node.val)
            node = node.next

        return values