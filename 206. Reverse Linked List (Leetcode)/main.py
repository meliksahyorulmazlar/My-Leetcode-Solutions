# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head

        while node is not None:
            values.append(node.val)

            node = node.next

        values = values[::-1]
        i = 0
        node = head

        while node is not None:
            node.val = values[i]
            print(node.val)
            i += 1

            node = node.next

        return head





