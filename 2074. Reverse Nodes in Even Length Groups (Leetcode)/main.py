# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lists = []

        new_list = []
        length = 1

        node = head

        while node is not None:
            new_list.append(node.val)
            if len(new_list) == length:
                lists.append(new_list)
                new_list = []
                length += 1
            node = node.next
        if len(new_list) > 0:
            lists.append(new_list)

        for i in range(len(lists)):
            if len(lists[i]) % 2 == 0:
                new_list = lists[i]
                new_list = new_list[::-1]
                lists[i] = new_list

        values = []
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                values.append(lists[i][j])

        new_head = ListNode(0)

        node = new_head
        for value in values:
            new_node = ListNode(value)
            node.next = new_node
            node = node.next

        return new_head.next

