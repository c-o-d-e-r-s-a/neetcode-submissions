# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #An alternative approach to this question will be using 2 pointers, we can keep an exact gap of n pointers between the front and the back nodes, that way as soon as we reach the end we are at the correct position and then we just delete the node

        #Initializing dummy node and the slow and fast nodes
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        #Spacing out the fast node by so that it always stays n nodes ahead of the slow node
        for i in range(n+1):
            fast = fast.next

        #Going till the end of the list
        while fast:
            fast = fast.next
            slow = slow.next

        #Deleting the node and linking to the next node
        slow.next = slow.next.next

        #This is the head of the list
        return dummy.next
        