from IPython.display import clear_output
import itertools
# Assigning players X or O
def start_func():
    p1 = input('Player1 : Please choose "X" or "O" :')
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    print('Player 1 will go first.')
    sin = input('Are you ready to play? Enter Yes or No.')
    if sin.lower() == 'yes':
        mylist = [' ',' ',' ',' ',' ',' ','','','']
        player_input(p1,p2,mylist)

#input_function()
def player_input(p1,p2,mylist):
     #
    game_end = 'False'
    curr_player = p1
    while game_end != 'True':
        if '' in mylist:
            clear_output()
            if curr_player == p1:
             display_board(mylist)
             in1 = input('Choose Your Next position: (1-9) ')
            else:
             display_board(mylist)
             in1 = input('Choose Your Next position: (1-9)')
            mylist[int(in1)-1] = curr_player
            game_end = checkifend(mylist,curr_player)
            if game_end == False:
                if curr_player == p1:
                 curr_player = p2
                else:
                 curr_player = p1
            else:
                print(f'Congratulations! {curr_player} has won the game.')

            game_end = checkifend(mylist,curr_player)
        else:
            print('The game has ended but sadly no one could win it!')

#Function to check if game has ended!
def checkifend(board,mark):
    # end_list =[[1,2,3],[1,4,7],[1,5,9],[3,6,9],[3,5,7],[7,8,9]]
    # indicesx = [ i for i, x in enumerate(mylist) if x == 'X']
    # indiceso = [ i for i, o in enumerate(mylist) if o == 'O']
    # if len(indicesx) >= 3 or len(indiceso) >= 3:
    #     for subend in end_list:
    #         rs = all(elem in indicesx for elem in subend)
    #         rs1 = all(elem in indiceso for elem in subend)
    #         if rs or rs1:
    #             return True
    #             break
    #         else:
    #             return False
    # else:
    #     return False
    return((board[0] == mark and board[1] == mark and board[2] == mark ) or
    (board[3] == board[4] == board[5] == mark) or
    (board[6] == board[7] == board[8] == mark) or
    (board[0] == board[3] == board[6] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[0] == board[4] == board[8] == mark) or
    (board[2] == board[4] == board[6] == mark))


def display_board(board):
    counter = 0
    for i in [0,1,2]:
        print('{0:^3}|{0:^3}|{0:^3}'.format(' '))
        print('{0:^3}|{1:^3}|{2:^3}'.format(board[counter+i],board[counter+i+1],board[counter+i+2]))
        print('{0:^3}|{0:^3}|{0:^3}'.format(' '))
        if i != 2:
            print('{0:-^3}|{0:-^3}|{0:-^3}'.format('-'))
        counter += 2

start_func()
