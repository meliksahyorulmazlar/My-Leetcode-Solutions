# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        values = []

        node = head
        values.append(node.val)

        while node is not None:
            try:
                next_node = node.next
                if next_node.val in values:
                    node.next = next_node.next
                    next_node.next = None
                else:
                    node = node.next
            except AttributeError:
                node.next = None
                node = None


        return head
