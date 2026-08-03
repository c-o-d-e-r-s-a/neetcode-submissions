class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #This solution is easier than the last one because we only need to go through the sudoku once, we will have 3 dictionaries/hash maps (rows, columns, and squares)
        #We can assign indexes to each square using the formula (r//3) * 3 + (c//3)

        rows = defaultdict(set) #Key is the row number and the value is all the numbers in that row
        columns = defaultdict(set) #Key is the column number and the value is all the numbers in that column
        squares = defaultdict(set) #Key is the index of the square (r//3)*3 + c//3 and value is all the numbers in that column

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue

                if board[row][column] in rows[row] or board[row][column] in columns[column] or board[row][column] in squares[(row//3) * 3 + column//3]:
                    return False

                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                squares[(row//3)*3 + column//3].add(board[row][column])

        return True
