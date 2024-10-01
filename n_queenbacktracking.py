def Is_Safe (board,row,col,N):
    i= col
    while i>=0:
        if board[row][i]==1:
            return False
        i-=1
    
    i=col
    j=row
    while i>=0 and j>=0:
        if board[j][i]==1:
            return False
        i-=1
        j-=1
    
    i=col
    j=row
    while i>=0 and j<N:
        if board[j][i]==1:
            return False
        i-=1
        j+=1

    return True


def solve_N_queen(board,col,N):
    
    if col>=N:
        return True
    for row in range(N):
        if Is_Safe(board,row=row,col=col,N=N):
            board[row][col]=1 

            if solve_N_queen(board,col+1,N):
                return True
            board[row][col]=0

    return False
            


N=4
board= [[0 for i in range(N)]for i in range(N)]
print(board)
if solve_N_queen(board=board,col=0,N=N):
    print(i for i in board)
print(board)                                                                    