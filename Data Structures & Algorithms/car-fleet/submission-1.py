class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #To calculate which cars will form a fleet we can use the time instead of adding up speed to the distance

        #Time = (target - position) / speed

        #Example 1: 2 entries
        #The first car will take (10 - 1)/3 = 3 units
        #The second car will take (10 - 4) / 2 = 3 units
        #Because both cars take the same time we can say that they will arrive the target at the same time and is a single fleet

        #Example 2: 3, 4.5, 0 , 3 -> are the time ech car takes
        #So the first car and the 3rd car will form a fleet and the other 2 do not take the same time so we can categorize them as different fleets

        #Sorting the position of the cars in desceneding order so we can pop as we know the time
        #Zip will only sort the position and not the speed because if we try to sort only the positions we will end up with mixed indices
        cars = sorted(zip(position, speed), reverse = True)

        #Initializing max_time to 0.0
        max_time = 0.0
        #Initializing fleets to 0
        fleets = 0

        for pos, speed in cars:
            
            #Calculating the time taken by each car
            time_to_target = (target - pos)/speed

            #If the time taken by the car is greater than our max time we know that it is going to be behind our last car and as the speed is not less than equal to that means we can categorize this as a whole different fleet

            if time_to_target > max_time:
                fleets += 1
                max_time = time_to_target

        return fleets




        
    


        