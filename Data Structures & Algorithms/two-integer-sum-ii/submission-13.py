class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Using Two pointers
        #Key here is if sum is too much bring the right to left
        #If sum is too little bring the left to right

        i = 0
        j = len(numbers) - 1

        while i < j:

            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]