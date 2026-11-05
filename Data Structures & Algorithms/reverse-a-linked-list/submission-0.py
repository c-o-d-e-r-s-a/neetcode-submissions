# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # Fix 1: Process until curr itself is None (handles empty lists safely too)
        while curr is not None:
            next_temp = curr.next
            curr.next = prev

            prev = curr
            curr = next_temp

        # Fix 2: prev is now at the new head (the old tail)
        return prev