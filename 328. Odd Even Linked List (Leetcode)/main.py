# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        odd = []

        index = 0

        node = head

        while node is not None:
            if index % 2 == 0:
                even.append(node.val)
            else:
                odd.append(node.val)

            node = node.next
            index += 1

        node = head
        while node is not None:
            if len(even) > 0:
                node.val = even[0]
                even.pop(0)
            else:
                node.val = odd[0]
                odd.pop(0)
            node = node.next

        return head
