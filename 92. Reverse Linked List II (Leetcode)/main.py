# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before = []
        middle = []
        after = []

        node = head
        count = 1
        while node is not None:
            if count < left:
                before.append(node.val)
            elif left <= count <= right:
                middle.append(node.val)
            else:
                after.append(node.val)
            count += 1
            node = node.next
        middle = middle[::-1]
        print(before, middle, after)
        items = before + middle + after
        new_head = ListNode(0)

        node = new_head
        for item in items:
            new_node = ListNode(item)
            node.next = new_node
            node = node.next

        return new_head.next


