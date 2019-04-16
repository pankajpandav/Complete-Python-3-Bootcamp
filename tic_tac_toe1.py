import random

def display_board(board):
    print('\n'*100)
    counter = 0
    for i in [1,2,3]:
        print('{0:^3}|{0:^3}|{0:^3}'.format(' '))
        print('{0:^3}|{1:^3}|{2:^3}'.format(board[counter+i],board[counter+i+1],board[counter+i+2]))
        print('{0:^3}|{0:^3}|{0:^3}'.format(' '))
        if i != 3:
            print('{0:-^3}|{0:-^3}|{0:-^3}'.format('-'))
        counter += 2


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
            marker = input('Player1, Please choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position between 1-9: '))

    return position


def place_marker(board,marker,position):

    board[position] = marker

def win_check(board,mark):

    return((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))


def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if  space_check(board,i):
            return False
    #BOARD IS FULL
    return True

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def replay():
    choice = input('Do you want to play again? Y or N: ')
    return choice == 'Y'


# Game start
#Game Setup
print('Welcome to Tic Tac Toe!')

while True:

    player1_marker,player2_marker = player_input()
    the_board = [' ']*10
    turn = choose_first()
    print(turn+' will go first')
    play_game = input('Ready to Play? Y or N : ')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #Player 1 turn
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            #Player 1 turn
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
