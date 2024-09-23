# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        node = head
        while node is not None:
            length += 1
            node = node.next

        position = (length // 2) + 1

        if length == 1:
            return head

        node = head
        count = 1
        while node is not None:
            if position - 1 == count:
                return node.next
            else:
                count += 1
                node = node.next