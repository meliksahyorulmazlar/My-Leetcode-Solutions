# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_values = []
        b_values = []

        node = headA
        while node is not None:
            a_values.append(node)
            node = node.next

        node = headB
        while node is not None:
            b_values.append(node)
            node = node.next

        for node in a_values:
            if node in b_values:
                return node

        return None



