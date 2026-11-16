class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        board =["."*n for _ in range(n)]
        leftrow=[0]*n
        upper_d=[0]*(2*n-1)
        lower_d=[0]*(2*n-1)
        self.solve(0,board,leftrow,upper_d,lower_d,ans,n)
        return ans

    def solve(self,col,board,leftrow,upper_d,lower_d,ans,n):
        if col==n:
            ans.append(board[:])
            return
        for row in range (n):  
            if (
                leftrow[row]==0 and
                lower_d[row+col]==0 and
                upper_d[n-1+col-row]==0
            ):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                leftrow[row]=1
                lower_d[row+col]=1
                upper_d[n-1+col-row]=1
                self.solve(col+1,board,leftrow,upper_d,lower_d,ans,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                leftrow[row]=0
                lower_d[row+col]=0
                upper_d[n-1+col-row]=0


        