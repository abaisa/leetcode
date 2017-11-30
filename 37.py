
def prevCell(a, b):
    if a == b == 0:
        return (-1, -1)
    if b > 0:
        return (a, b-1)
    return (a-1, 8)

def nextCell(a, b):
    if a == b == 8:
        return (-1, -1)
    if b < 8:
        return (a, b+1)
    return (a+1, 0)

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
"""
:type board: List[List[str]]
:rtype: void Do not return anything, modify board in-place instead.
"""
A = [[False for i in range(9)] for j in range(9)]
B = [[False for i in range(9)] for j in range(9)]
C = [[False for i in range(9)] for j in range(9)]
FLAG = [[0 for i in range(9)] for j in range(9)]

#0->given 1->empty 2->filled
for i in range(9):
    for j in range(9):
        if board[i][j] == '.':
            FLAG[i][j] = 1
        else:
            num = int(board[i][j]) - 1 
            blockId = int(i // 3 * 3 + j // 3)
            A[i][num] = B[j][num] = C[blockId][num] = True

a, b = 0, 0
while a >= 0:
    if FLAG[a][b] == 0:
        a, b = self.nextCell(a, b)
    elif FLAG[a][b] == 1:
        fillNum, flag = 0, 0
        for fillNun in range(9):
            if not (A[i][fillNum] or B[j][fillNum] or C[blockId][fillNum]):
                A[i][fillNum] = B[j][fillNum] = C[blockId][fillNum] = True
                board[a] = str(board[a][:b]) + str(fillNum+1) + str(board[a][b+1:])
                flag = 1
        if flag == 0:
            a, b = prevCell(a, b)
        else:
            a, b = nextCell(a, b)
            FLAG[a][b] = 2
    elif FLAG[a][b] == 2:
        origNum = int(board[a][b]) - 1
        A[i][origNum] = B[j][origNum] = C[blockId][origNum] = False
        fillNum, flag = 0, 0
        for fillNun in range(origNum, 9):
            if not (A[i][fillNum] or B[j][fillNum] or C[blockId][fillNum]):
                A[i][fillNum] = B[j][fillNum] = C[blockId][fillNum] = True
                board[a] = str(board[a][:b]) + str(fillNum+1) + str(board[a][b+1:])
                flag = 1
        if flag == 0:
            a, b = prevCell(a, b)
            FLAG[a][b] = 1
        else:
            a, b = nextCell(a, b)
    