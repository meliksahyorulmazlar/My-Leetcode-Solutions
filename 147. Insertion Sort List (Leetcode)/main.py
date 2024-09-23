# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        values = sorted(values)

        new_head = ListNode(0)
        node = new_head
        for value in values:
            new_node = ListNode(value)
            node.next = new_node
            node = node.next

        return new_head.next    
