# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        numbers = []
        node = head

        while node is not None:
            numbers.append(str(node.val))
            node = node.next

        number = int(str("".join(numbers))) + 1
        number = str(number)
        print(number)
        new_list = [int(n) for n in list(number)]

        new_head = ListNode(0)

        node = new_head

        for i in range(len(new_list)):
            new_node = ListNode(new_list[i])
            node.next = new_node
            node = node.next

        return new_head.next
