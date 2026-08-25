class Solution:

    #Optimal solution O(n)

    def longestConsecutive(self, nums: List[int]) -> int:

        count = 1
        temp = 0

        mySet = set(nums)

        for num in mySet:

            if num-1 in mySet:
                continue
                
            else:

                myNum = num

                while myNum + 1 in mySet:
                    count += 1
                    myNum += 1

                temp = max(temp, count)

                count = 1

        
        return temp


        