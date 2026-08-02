class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        myDict = {}
        
        # Checking the rows
        for i in range(0, len(board)):
            if not self.checkRows(board[i]):
                return False
                
        # Checking the columns
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if not board[j][i] == ".":
                    val = int(board[j][i])
                    if board[j][i] in myDict or val < 1 or val > 9:
                        return False
                    else:
                        myDict[board[j][i]] = 1
            myDict = {}  # Cleared after every column pass
            
        # Checking the boxes
        for rowBlock in range(3):
            for colBlock in range(3):
                rowStart = rowBlock * 3
                rowEnd = rowStart + 3
                start = colBlock * 3
                end = start + 3
                
                for i in range(rowStart, rowEnd):
                    for j in range(start, end):
                        if not board[i][j] == ".":
                            val = int(board[i][j])
                            if board[i][j] in myDict or val < 1 or val > 9:
                                return False
                            else:
                                myDict[board[i][j]] = 1
                myDict = {}  # Cleared after every 3x3 box pass
                
        return True

    def checkRows(self, row: List[str]) -> bool:
        myDict = {}
        for i in range(0, len(row)):
            if not row[i] == ".":
                val = int(row[i])
                if row[i] in myDict or val < 1 or val > 9:
                    return False
                else:
                    myDict[row[i]] = 1
        return True