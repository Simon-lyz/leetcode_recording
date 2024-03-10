class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            storaged = []
            for j in range(9):
                if board[i][j].isalnum():
                    if board[i][j] in storaged:
                        return False
                    else:
                        storaged.append(board[i][j])

        print('done')
        for i in range(9):
            storaged = []
            for j in range(9):
                if board[j][i].isalnum():
                    if board[j][i] in storaged:
                        return False
                    else:
                        storaged.append(board[j][i])

        print('done')
        for i in range(0,9,3):
            for j in range(0,9,3):
                storaged = []
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y].isalnum():
                            if board[x][y] in storaged:
                                return False
                            else:
                                storaged.append(board[x][y])
        print('done')
        return True