# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head

        values = []
        while node is not None:
            values.append(node.val)
            node = node.next

        values = values[::-1]
        total = sum([pow(2, i) for i in range(len(values)) if values[i] == 1])
        return total
