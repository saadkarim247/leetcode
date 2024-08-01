class Solution:
    def containsAllNumbers(self, board: List[List[str]]) -> bool:
        store = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                item = board[i][j]
                if item in store and not item == ".":
                    return False
                else:
                    store[item] = tuple([i, j])
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            storeRow = {}
            for j in range(len(board[0])):
                itemRow = board[i][j]
                if itemRow in storeRow and not itemRow == ".":
                    return False
                else:
                    storeRow[itemRow] = tuple([i, j])

        for l in range(len(board)):
            storeColumn = {}
            for j in range(len(board[0])):
                itemColumn = board[j][l]
                if itemColumn in storeColumn and not itemColumn == ".":
                    
                    return False
                else:
                    storeColumn[itemColumn] = tuple([l, j])

        for x in range(0, 7, 3):
            for z in range(0, 7, 3):
                if not self.containsAllNumbers(
                    [
                        board[x][z : z + 3],
                        board[x + 1][z : z + 3],
                        board[x + 2][z : z + 3],
                    ]
                ):
                    return False
        return True
        
        