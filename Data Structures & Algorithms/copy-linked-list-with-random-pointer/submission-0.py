"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        myDict = {}
        myDict[None] = None

        current = head

        while current != None:

            if current in myDict:
                continue
            else:
                myDict[current] = Node(current.val)
            
            current = current.next
        
        current = head

        while current != None:

            myDict[current].next = myDict[current.next]
            myDict[current].random = myDict[current.random]

            current = current.next

        return myDict[head]
        


        