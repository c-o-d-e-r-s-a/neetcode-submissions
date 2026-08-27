class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #We will use the 2 pointer technique in this problem. 
        #We need to sort the list first
        #We will go through every element using a for loop
        #We will have 2 pointers, one will start at the next element of the i(in for loop) and one will start at the right end
        #We keep adding these 2 pointers and the current element at i, if sum < 0, we increase the position of the left pointer by 1 because we need a bigger number to make the sum 0
        #If we get sum > 0 then we will take the right most pointer one position to the left
        #If the sum of these three elements = 0, we will add it to the set as a , also check if this sequence already exists in the set
        nums = sorted(nums)
        myList = []

        for i in range(len(nums)):
            
            if i != 0 and nums[i] == nums[i-1]:
                 continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    myList.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1
                
                else:
                    right -= 1

        return myList
                    