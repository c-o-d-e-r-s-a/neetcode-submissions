# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #The previous solution used O(n) space, this solution's space complexity is O(1)

        #We can  split the linked list into two halves using slow and fast pointers. Slow pointer moves by 1 node and the fast pointer moves by 2 nodes
        #Then we can reverse the second half of the linked list
        #Then we can merge alternate nodes from both the front and reversed back to get our solution

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
