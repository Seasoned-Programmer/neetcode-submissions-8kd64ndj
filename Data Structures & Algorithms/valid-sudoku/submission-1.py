class Solution:
    def checkSquare(self,arr):
        Res = True;
        box = list()
        for i in range(3):
            for j in range(3):
                if arr[i][j] != ".":
                    if arr[i][j] in box:
                        Res = False
                    else:
                        box.append(arr[i][j])
        return Res
                    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        res = False
                        break
                    else :
                        row.append(board[i][j])
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in col:
                        res = False
                        break
                    else:
                        col.append(board[j][i])

        for i in range(0,9,3):
            for j in range (0,9,3):
                square = [row[i:i+3] for row in board[j:j+3]]
                if not(self.checkSquare(square)):
                    res = False
                    break

        return res
                    


        