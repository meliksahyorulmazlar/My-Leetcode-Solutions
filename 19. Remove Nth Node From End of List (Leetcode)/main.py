# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        values = []
        node = head

        while node is not None:
            values.append(node.val)

            node = node.next

        skip = values[-n]

        node = head
        while node is not None:
            if node.next.val == skip:
                node = node.next.next
            else:
                node = node.next

        return head
