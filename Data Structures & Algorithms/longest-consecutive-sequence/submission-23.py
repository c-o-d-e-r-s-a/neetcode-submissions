class Solution:

    #Optimal Solution, O(n) space and time

    def longestConsecutive(self, nums: List[int]) -> int:

        #Remove duplicates and store every unique number in a set, a set is better than a hash map
        numSet = set(nums)
        longest = 0

        for num in numSet:
            #Check if the number is the start of the sequence
            if (num - 1) not in numSet:
                length = 1

                #Keep adding to the length till sequence exists
                while (num + length) in numSet:
                    length += 1

                #Keep the longest sequence
                longest = max(length, longest)

        return longest