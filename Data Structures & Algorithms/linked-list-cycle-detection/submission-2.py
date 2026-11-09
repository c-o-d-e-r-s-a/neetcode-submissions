# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Using a set is better because we are only saving the nodes and not mapping and values

#To make the space O(1) from O(n) we can use Floyd's algorithm using a slow and a fast pointer which says if there is a cycle there will eventually be a point when the slow pointer and the fast pointer will meet. The slow pointer moves one node at a time and the fast pointer moves 2 nodes at a time

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False