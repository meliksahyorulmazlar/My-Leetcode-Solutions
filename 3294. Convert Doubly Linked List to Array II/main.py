"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""


class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        values = []
        current_node = node
        while current_node is not None:
            print(current_node.val)
            if current_node.prev is None:
                break
            else:
                current_node = current_node.prev

        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next

        return values
