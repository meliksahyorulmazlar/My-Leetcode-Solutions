# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for l in lists:
            head = l
            node = head
            while node is not None:
                values.append(node.val)
                node = node.next

        values = sorted(values)

        head = ListNode(0)
        index = 0
        node = head

        while index != len(values):
            new_node = ListNode(values[index])
            node.next = new_node
            index += 1
            node = node.next

        return head.next




