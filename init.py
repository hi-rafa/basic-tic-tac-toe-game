from __future__ import print_function
from IPython.display import clear_output

def display_board(board):
    clear_output()
    row = ''
    for idx,column in enumerate(board):
        #print(idx)
        idx += 1
        column = str(column) if str(column) == 'X' or str(column) == 'O' else idx 
        if( (idx % 3) == 0 ):
            row += '|' + str(column) + '|'
            print (row)
            row = ''
        else:
            row += '|' + str(column)
    pass


def replay():
    replay = True if raw_input('Wanna play again?') == 'yes' else False
    return replay;

def space_check(board, position):
    return False if board[position] != 'X' or board[position] != 'O' else True


def full_board_check(board):
    for cell in board:
        if cell != 'X' or cell != 'O':
            return False
    return True

def player_choice(board):
    input_position = input('Choose a position between (1 to 9): ')
    input_position = input_position if space_check(board, (input_position-1)) != True else False
    return input_position


def place_marker(board, marker, position):
    board[position-1] = marker
    pass

def player_input(player):
    global board
    position = player_choice(board)
    if not (position):
        return False
    place_marker(board,player,position)
    return True

def win_check(board,marker):
    if (board[0] == board[1] == board[2] == marker):
        return True
    elif (board[3] == board[4] == board[5] == marker):
        return True
    elif (board[6] == board[7] == board[8] == marker):
        return True
    elif (board[0] == board[3] == board[6] == marker):
        return True
    elif (board[1] == board[4] == board[7] == marker):
        return True
    elif (board[2] == board[5] == board[8] == marker):
        return True
    elif (board[0] == board[4] == board[8] == marker):
        return True
    elif (board[2] == board[4] == board[6] == marker):
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')


while True:
    print ("Rafa's game!")
    # Set the game up here
    game_on = True;
    board  = [''] * 9
    #pass

    while game_on:
        #Player 1 Turn
        player1 = False
        while (player1 == False):
            player1 = player_input('X')
            print ( player1 ) 
        display_board(board)
        print ('display_board')
        player1_win = win_check(board,'X')
        if (player1_win):
            print ('WINNER PLAYER 1')
            break
        
        # Player2's turn.
        player2 = False
        while (player2 == False):
            player2 = player_input('O')
            print ( player2 ) 
        display_board(board)
        print ('display_board')
        player2_win = win_check(board,'O')
        if (player2_win):
            print ('WINNER PLAYER 2')
            break
            
        if (full_board_check(board)): break

    if not replay():
        break
