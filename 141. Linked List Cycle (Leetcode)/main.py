# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        values = []
        node = head
        values.append(node.val)
        node = node.next
        while node is not None:
            value = node.val
            if value not in values:
                values.append(value)
            else:
                return True

        return False
