# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        node = head
        while node is not None:
            if node not in nodes:
                nodes.append(node)
            else:
                return node
            node = node.next

        return None
