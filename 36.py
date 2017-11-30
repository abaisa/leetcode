class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Three tables, record line, row, block,and the num is used
        A = [[False for i in range(9)] for j in range(9)]
        B = [[False for i in range(9)] for j in range(9)]
        C = [[False for i in range(9)] for j in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    blockId = int(i // 3 * 3 + j // 3)
                    if(A[i][num] or B[j][num] or C[blockId][num]):
                        return False
                    A[i][num] = B[j][num] = C[blockId][num] = True
        return True