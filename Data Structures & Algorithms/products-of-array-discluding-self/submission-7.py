class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #go through the whole array and make a dict
        #if there are more than 1 zero return an array of 0s
        #Else if there is just one zero then return the product in the zero index and 0s in other index
        #If no zeroes then we will use division
        product = 1
        myDict = {}

        for num in nums:
            if num != 0:
                product *= num
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1

        if 0 in myDict:

            if myDict[0] > 1:
                for i in range(0, len(nums)):
                    nums[i] = 0
                return nums
            
            else:
                for i in range(0, len(nums)):
                    if(nums[i] == 0):
                        nums[i] = product
                    else:
                        nums[i] = 0
                return nums

        else:

            for i in range(0, len(nums)):
                nums[i] = product//nums[i]
            return nums
        

