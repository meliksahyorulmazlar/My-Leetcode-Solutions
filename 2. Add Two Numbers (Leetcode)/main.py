# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1 = ""
        current = l1
        while current is not None:
            string1 += str(current.val)
            current = current.next

        string2 = ""
        current = l2
        while current is not None:
            string2 += str(current.val)
            current = current.next

        total = int(string1[::-1]) + int(string2[::-1])
        total = str(total)
        total = [int(char) for char in total]

        total = total[::-1]
        dummy_head = ListNode(0)
        current = dummy_head

        for digit in total[1:]:
            current.next = ListNode(digit)
            current = current.next

        return dummy_head.next
