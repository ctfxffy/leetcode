class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        isTransfer = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        dx=[0,1,-1]
        dy=[0,1,-1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                countOfone=0
                for delta_x in dx:
                    for delta_y in dy:
                        if delta_x==0 and delta_y==0:
                            continue
                        if i+delta_x <0 or i+delta_x>=len(board) or j+delta_y<0 or j+delta_y>=len(board[0]):
                            continue
                        if board[i+delta_x][j+delta_y]==1:
                            countOfone=countOfone+1
                        
                if board[i][j]==1 and countOfone<2:
                    isTransfer[i][j]=1
                if board[i][j]==1 and (countOfone==2 or countOfone==3):
                    isTransfer[i][j]=0
                if board[i][j]==1 and countOfone>3:
                    isTransfer[i][j]=1
                if board[i][j]==0 and countOfone==3:    
                    isTransfer[i][j]=1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if isTransfer[i][j]==1:
                    if board[i][j]==1:board[i][j]=0
                    else:board[i][j]=1
