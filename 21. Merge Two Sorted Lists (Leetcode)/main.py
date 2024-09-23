# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        node = list1

        while node is not None:
            values.append(node.val)

            node = node.next

        node = list2

        while node is not None:
            values.append(node.val)

            node = node.next

        values = sorted(values)

        head = ListNode(0)

        index = 0

        node = head
        while index != len(values):
            next_node = ListNode(values[index])
            node.next = next_node
            node = next_node
            print(values[index])
            index += 1

        return head.next




