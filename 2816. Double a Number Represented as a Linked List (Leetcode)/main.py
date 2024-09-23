# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys

# Increase the limit for integer string conversion
sys.set_int_max_str_digits(100000000)


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers = []

        node = head

        while node is not None:
            numbers.append(node.val)
            node = node.next

        number = int("".join([str(n) for n in numbers]))
        number *= 2

        number_list = [int(n) for n in list(str(number))]

        dummy_head = ListNode(0)

        node = dummy_head
        for n in number_list:
            new_node = ListNode(n)
            node.next = new_node
            node = node.next

        return dummy_head.next


