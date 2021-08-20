#https://leetcode.com/problems/valid-sudoku/submissions/
def isValidSudoku(board):
    # checking if row contents are unique
    for i in  range(0,9):
        row=[]
        for j in range(0,9):
            if board[i][j] != '.':
                if board[i][j] in row:
                    print(board[i][j],' repeated')
                    return False
                else:
                    row.append(board[i][j])
    
    # checking if column contents are unique
    for i in  range(0,9):
        col=[]
        for j in range(0,9):
            if board[j][i] != '.':
                if board[j][i] in col:
                    print(board[j][i],' repeated')
                    return False
                else:
                    col.append(board[j][i])
                    
    # checking 3X3 
    cnt,k,i,=0,0,0
    while(cnt<9):
        op=[]
        for i in range(i,3+i):
            for k in range(k,3+k):
                if board[i][k] != '.':
                    if board[i][k] in op:
                        print(board[i][k],' repeated')
                        return False
                    else:
                        op.append(board[i][k])
            k=k-2 # sticking to the current column 
        i=i+1
       
            
        k=k+3 #to move to the second 3X3 
        cnt=cnt+1 
        if k>8:
           k=0 # to begin the second 3X3
        else:
            i=i-3 # to ensure we are still on the starting row
            
        
                        
            
            
    return True       
print(isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))#T
board =[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]            
print(isValidSudoku(board))#F
