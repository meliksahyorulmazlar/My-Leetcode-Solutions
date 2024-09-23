# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        node = head

        while node is not None:
            length += 1
            node = node.next
        node = head
        count = 0
        position = 0

        if length == 1:
            return
        position = (length // 2) + 1

        while node is not None:
            count += 1
            if position - 1 == count:
                next_node = node.next
                node.next = next_node.next
                next_node.next = None
            node = node.next

        return head
