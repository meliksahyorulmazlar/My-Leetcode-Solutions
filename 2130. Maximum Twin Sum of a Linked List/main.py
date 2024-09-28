# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        greatest = 0
        for i in range(len(values) // 2):
            value1 = values[i]
            value2 = values[len(values) - i - 1]
            value = value1 + value2
            if value > greatest:
                greatest = value

        return greatest