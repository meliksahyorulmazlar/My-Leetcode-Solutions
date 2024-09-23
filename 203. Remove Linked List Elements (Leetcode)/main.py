# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        values = []
        node = head

        while node is not None:
            values.append(node.val)
            node = node.next

        values = [v for v in values if v!=val]

        new_head = ListNode(0)
        node = new_head
        index = 0
        while index != len(values):
            new_node = ListNode(values[index])
            node.next = new_node
            index += 1
            node = node.next

        return new_head.next
