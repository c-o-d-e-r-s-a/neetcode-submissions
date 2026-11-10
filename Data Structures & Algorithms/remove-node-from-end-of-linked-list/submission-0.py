class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Pass 1: Find the total length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Edge case: If n equals the length, we are deleting the head node
        if length == n:
            return head.next
        
        # Pass 2: Traverse to the node just BEFORE the one we want to delete
        # We need to reach index: length - n - 1 (0-indexed)
        curr = head
        for i in range(length - n - 1):
            curr = curr.next
        
        # Skip/delete the target node
        curr.next = curr.next.next
        
        return head