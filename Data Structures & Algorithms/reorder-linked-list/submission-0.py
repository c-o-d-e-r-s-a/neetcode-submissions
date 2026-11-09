# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        myList = []
        index = 0
        current = head

        while current != None:
            
            myList.append(current)
            current = current.next
            index += 1

        dummy = ListNode()
        current = dummy

        for i in range(0, len(myList)):
            if i % 2 == 0:
                current.next = myList[i//2]
            else:
                current.next = myList[(len(myList) - 1 - (i//2))]
            
            current = current.next
        
        current.next = None