# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node is not None:
            next_node = node.next
            if next_node is None:
                node = node.next
            else:
                next_value = next_node.val
                current_value = node.val
                values = [1]
                for i in range(2, max(next_value, current_value) + 1):
                    if (next_value % i) == 0 and (current_value % i) == 0:
                        values.append(i)
                print(max(values))
                new_node = ListNode(max(values))
                node.next = new_node
                new_node.next = next_node
                node = next_node

        return head