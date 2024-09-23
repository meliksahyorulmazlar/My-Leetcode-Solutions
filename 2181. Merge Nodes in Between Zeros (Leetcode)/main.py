# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        value = 0

        node = head
        node = node.next

        while node is not None:
            node_value = node.val
            if node_value == 0:
                values.append(value)
                value = 0
            else:
                value += node_value

            node = node.next

        node = head

        for i in range(len(values)):
            if i == len(values) - 1:
                node.val = values[i]
                node.next = None
            else:
                node.val = values[i]
                node = node.next

        node.next = None

        return head

