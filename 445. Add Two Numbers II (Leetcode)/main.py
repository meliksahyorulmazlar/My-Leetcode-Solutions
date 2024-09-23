# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = []
        number2 = []

        node = l1

        while node is not None:
            number1.append(str(node.val))
            node = node.next

        node = l2

        while node is not None:
            number2.append(str(node.val))
            node = node.next

        num1 = int("".join(number1))
        num2 = int("".join(number2))

        result = str(num1 + num2)
        numbers = [int(n) for n in list(result)]

        new_head = ListNode(0)
        node = new_head
        for number in numbers:
            new_node = ListNode(number)
            node.next = new_node
            node = node.next

        return new_head.next

