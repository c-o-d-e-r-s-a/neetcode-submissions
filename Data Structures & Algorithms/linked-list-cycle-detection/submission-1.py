# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Using a set is better because we are only saving the nodes and not mapping and values
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        mySet = set()
        current = head

        while current != None:

            if current not in mySet:
                mySet.add(current)
            else:
                return True

            current = current.next

        return False
        