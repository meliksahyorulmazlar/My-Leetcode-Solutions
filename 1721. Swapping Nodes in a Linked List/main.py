# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []

        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        a = values[k - 1]
        b = values[-k]

        values[k - 1] = b
        values[-k] = a

        dummy_head = ListNode(0)
        node = dummy_head
        for i in range(len(values)):
            new_node = ListNode(values[i])
            node.next = new_node
            node = node.next

        return dummy_head.next


