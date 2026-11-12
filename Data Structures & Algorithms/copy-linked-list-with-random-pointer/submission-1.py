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
        if not head:
            return None

        myDict = {}
        
        # First pass: Create a copy of every node and map original -> copy
        current = head
        while current != None:
            myDict[current] = Node(current.val)
            current = current.next
        
        # Second pass: Wire up the next and random pointers using the dictionary
        current = head
        
        while current != None:
            #.get() will return None if key does not exist so this prevents a key error
            myDict[current].next = myDict.get(current.next)
            myDict[current].random = myDict.get(current.random)
            current = current.next
        
        return myDict[head]
        


        