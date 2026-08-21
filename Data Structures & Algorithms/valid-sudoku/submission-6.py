class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        myCol = {}
        myRow = {}
        myBox = {}

        for row in range(0,9):

            for col in range(0,9):
            
              if board[row][col] != ".":

                if row in myRow:
                    if board[row][col] in myRow[row]:
                        return False
                    else:
                        myRow[row].append(board[row][col])
                else:
                    myRow[row] = [board[row][col]]

        
                if col in myCol:
                    if board[row][col] in myCol[col]:
                        return False
                    else:
                        myCol[col].append(board[row][col])
                else:
                    myCol[col] = [board[row][col]]

                box = ((col) // 3) + (row // 3) * 3

                if box in myBox:
                    if board[row][col] in myBox[box]:
                        return False
                    else:
                        myBox[box].append(board[row][col])
                else:
                    myBox[box] = [board[row][col]]

        return True