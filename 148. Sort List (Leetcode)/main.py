# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        values = sorted(values)
        node = head
        for value in values:
            node.val = value
            node = node.next

        return head