class Solution(object):
    def make_board(self):
        board = []
        
        for i in range(3):
            board.append([])
            for j in range(3):
                board[i].append("")
        
        return board
    
    def check_row(self,board,row,player):
        return board[row][0] == player and board[row][1] == player and board[row][2] == player 
        
        
    def check_col(self,board,col,player):
        return board[0][col] == player and board[1][col] == player and board[2][col] == player 
        
    def check_diagonal(self,board,flag,player):
        if flag:
            return board[0][0] == player and board[1][1] == player and board[2][2] == player
        else:
            return board[0][2] == player and board[1][1] == player and board[2][0] == player
        
    def tictactoe(self, moves):
        count_A = 0
        count_B = 0
        
        board = self.make_board()
        
        i = 1
        
        for each in moves:
            if i % 2 != 0:
                board[each[0]][each[1]] = "X"
                count_A += 1
            else:
                board[each[0]][each[1]] = "O"
                count_B += 1
                
            i += 1
            
        out = (False,"Pending")
        
        if len(moves) % 2 == 0:
            flag = False
            
            for row in range(3):
                flag = flag or self.check_row(board,row,"O")
                flag = flag or self.check_col(board,row,"O")
                
            flag = self.check_diagonal(board,True,"O") or self.check_diagonal(board,False,"O") or flag
            
            out = (True,"B") if flag else (False,"Draw")
        
        else:
            flag = False
            
            for row in range(3):
                flag = flag or self.check_row(board,row,"X")
                flag = flag or self.check_col(board,row,"X")
            
            flag = self.check_diagonal(board,True,"X") or self.check_diagonal(board,False,"X") or flag
            
            out = (True,"A") if flag else (False,"Draw")
            
        if out[0] == True:
            return out[1]
        else:
            if count_A + count_B == 9:
                return "Draw"
            else:
                return "Pending"
        
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        