#CSE 210 - Tic-Tac-Toe / Week 2 - Thiago Leite.

make_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in make_board:
    board_keys.append(key)

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def main():

    turn = 'X'
    count = 0


    for i in range(10):
        print_board(make_board)
        print("It's your turn," + turn + ".Move to which place?")
        print()

        move = input()        

        if make_board[move] == ' ':
            make_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        
        count_score(count, turn)

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 
    
def count_score(count, turn):

        if count >= 5:
            if make_board['7'] == make_board['8'] == make_board['9'] != ' ': # across the top
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['4'] == make_board['5'] == make_board['6'] != ' ': # across the middle
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['1'] == make_board['2'] == make_board['3'] != ' ': # across the bottom
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['1'] == make_board['4'] == make_board['7'] != ' ': # down the left side
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['2'] == make_board['5'] == make_board['8'] != ' ': # down the middle
                print_board(make_board())
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['3'] == make_board['6'] == make_board['9'] != ' ': # down the right side
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['7'] == make_board['5'] == make_board['3'] != ' ': # diagonal
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
            elif make_board['1'] == make_board['5'] == make_board['9'] != ' ': # diagonal
                print_board(make_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
  

if __name__ == "__main__":
    main()