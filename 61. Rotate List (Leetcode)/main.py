# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        values = []

        node = head

        while node is not None:
            values.append(node.val)
            node = node.next

        if k > len(values):
            k = k % len(values)

        if len(values) == k:
            return head
        else:
            for i in range(k):
                value = values.pop()
                values.insert(0, value)

        head = ListNode(0)
        node = head
        index = 0

        while index != len(values):
            new_node = ListNode(values[index])
            node.next = new_node
            index += 1
            node = node.next

        return head.next














