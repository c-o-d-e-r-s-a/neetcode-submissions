class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#This solution uses bitmask where we have an array of values (like a 8 bit integer), whenever we get a value we turn the switch for that position and then compare, if the value exists return false else we add that value to the array. At the end return True if all values are correctly assigned

        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):

            for c in range(9):

                if board[r][c] == ".":
                    continue

                #We will use 0-8 as the positions
                val = int(board[r][c]) - 1

#1<<val shifts the turned on switch to its correct position and creates a mask. The &(bitwise operator) compares this mask against the tracking integer for the current row rows[r]

#If the result is not 0, the bit was already turned on. A duplicate exists in this row, so it terminates early and returns False.

                if (1 << val) & rows[r]:
                    return False


#exact same check for the current column tracker cols[c].
                if (1 << val) & cols[c]:
                    return False

#exact same check for the current square tracker square[(r//3)*3 + c//3].
                if (1 << val) & squares[(r//3) * 3 + c//3]:
                    return False

#If the values is not in the list then we turn on the switch using the statements below
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r//3) * 3 + c//3] |= (1 << val)

        return True

                

