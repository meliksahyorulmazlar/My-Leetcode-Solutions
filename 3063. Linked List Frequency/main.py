# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dictionary = {}
        node = head

        while node is not None:
            value = node.val
            if value in dictionary:
                dictionary[value] += 1
            else:
                dictionary[value] = 1
            node = node.next

        values = [dictionary[k] for k in dictionary]

        head = ListNode(0)
        node = head

        for i in range(len(values)):
            new_node = ListNode(values[i])
            node.next = new_node
            node = node.next

        return head.next
