class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []

        #We are using a deque for this question, it is a monotically decreasing queue

        q = collections.deque()
        l = r = 0 #Pointers for our window

        while r < len(nums):

            #Remove all the elements from the right of the queue that are the smaller than the element we are adding because we will never have to look at them again
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            #Removing the left element from the queue if our window has moved on
            if q[0] < l:
                q.popleft()
            
            #If the window is greater than or = the window size we will add the leftmost element from the queue to our output list and shift our window from the left forward

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            
            #Moving the right pointer ahead to increase window size
            r += 1

        return output

            

            

            




