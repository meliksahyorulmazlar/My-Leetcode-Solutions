# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd_points = 0
        even_points = 0
        node = head
        while node is not None:
            even = node.val
            odd = node.next.val
            if odd > even:
                odd_points += 1
            else:
                even_points += 1

            node = node.next.next

        if odd_points == even_points:
            return "Tie"
        elif odd_points > even_points:
            return "Odd"
        else:
            return "Even"
