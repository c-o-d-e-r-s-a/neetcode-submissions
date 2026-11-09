# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        myDict = {}
        current = head

        while current != None:

            if current not in myDict:
                myDict[current] = 1
            else:
                return True

            current = current.next

        return False
        