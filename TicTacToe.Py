print("Welcome to the Animesh's tic tac toe game. ")
print("| | |")
print("\n| | |")
print("\n| | |")
Player1 = input("Player 1 !! please select X or O ")
Player2 = 'twmp'
print("Player 1 , You selected", Player1)
if Player1 == 'X' or 'x':
    Player2 = 'O'
elif Player1 == 'O' or 'o':
    Player2 = 'X'
else:
    print("Invalid input selected")
print("Player 2 , By default is "+Player2 )
"""
print("| | |")
print("\n| | |")
print("\n| | |")


"""
board=[""]*10

def winningCombination(board):
    if((board[0]==board[1] and board[1]==board[2] and (board[1] == 'X'or board[1] =='O') ) or
       (board[3]==board[4] and board[4]==board[5] and (board[3] == 'X'or board[3] =='O') ) or
       (board[6]==board[7] and board[7]==board[8] and (board[6] == 'X'or board[6] =='O')) or
       (board[0]==board[4] and board[4]==board[8] and (board[0] == 'X'or board[0] =='O')) or
       (board[0]==board[3] and board[3]==board[6] and (board[0] == 'X'or board[0] =='O')) or
       (board[1]==board[4] and board[4]==board[7] and (board[1] == 'X'or board[1] =='O')) or
       (board[2]==board[5] and board[5]==board[8] and (board[2] == 'X'or board[2] =='O')) or
       (board[2]==board[4] and board[4]==board[6] and (board[2] == 'X'or board[2] =='O'))):
        return True
    else:
        return False

def printBoard(board):
    print(board[0] +"|" +  board[1] + "|" + board[2])
    print("\n"+board[3] +"|" +  board[4] + "|" + board[5])
    print("\n"+board[6] +"|" +  board[7] + "|" + board[8])
    
count =0
while(winningCombination(board)==False):
    
    player1turn = input("Player 1 , Please play your turn (1-9)")
    board[int(player1turn)-1]=Player1
    
    printBoard(board)
    if(winningCombination(board)==True):
        break
    
    player2turn = input("Player 2 , Please play your turn (1-9)")
    board[int(player2turn)-1]=Player2
    count+=1
    
    printBoard(board)

    if (count==9):
        break
    
print("game end")

