class MinStack:

    def __init__(self):

        #Assigning object to a list because a stack is basically a list with the LIFO approach
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        #Appending to the stack at the very top
        self.stack.append(val)

        #For every push in the stack, we push the current minimum of the whole stack to min_stack, its like for every push you save the minimum element at that point for the whole stack, like this we have the same height for both the stacks and we can return the minimum value efficiently even when popping
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        #We need to pop from the min_stack as well because we need to keep the same height of both the stacks and remove any element that is not in our original stack
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
