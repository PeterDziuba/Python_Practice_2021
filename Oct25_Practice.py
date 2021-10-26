import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in board:
        print(i)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    print("Your turn!\n")
    o_move = str(input("Where would you like to play?\n"))
    try:
        if o_move == "1":
            if board[0][0] != "X" and board[0][0] != "O":
                board[0][0] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
        elif o_move == "2":
            if board[0][1] != "X" and board[0][1] != "O":
                board[0][1] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
        elif o_move == "3":
            if board[0][2] != "X" and board[0][2] != "O":
                board[0][2] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
        elif o_move == "4":
            if board[1][0] != "X" and board[1][0] != "O":
                board[1][0] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
                
        elif o_move == "5":
            print("Invalid entry")
            enter_move(board)
            
        elif o_move == "6":
            if board[1][2] != "X" and board[1][2] != "O":
                board[1][2] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
                
        elif o_move == "7":
            if board[2][0] != "X" and board[2][0] != "O":
                board[2][0] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
                
        elif o_move == "8":
            if board[2][1] != "X" and board[2][1] != "O":
                board[2][1] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
                
        elif o_move == "9":
            if board[2][2] != "X" and board[2][2] != "O":
                board[2][2] = "O"
                return board
            else:
                print("Invalid entry")
                enter_move(board)
                
        else:
            print("Invalid entry")
            enter_move(board)
        
    except:
        print("Invalid entry")
        enter_move(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    my_list = []
    for i in board:
        my_list.append(i)
    return tuple(my_list)

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in board:
        if i[0] == i[1] and i[1] == i[2]:
            print(str(i[0]),"won!")
            return True
            
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print(str(board[0][0]),"won!")
        return True
        
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print(str(board[0][0]), "won!")
        return True
        
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            print(str(board[0][i]), "won!")
            return True
            
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    comp_move = str(random.randrange(1, 9))
    my_list = make_list_of_free_fields(board)
    if len(my_list) < 1:
        print("Draw")
        return
    
    try:
        if comp_move == "1":
            if board[0][0] != "X" and board[0][0] != "O":
                print("Computer chose 1!")
                board[0][0] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "2":
            if board[0][1] != "X" and board[0][1] != "O":
                print("Computer chose 2!")
                board[0][1] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "3":
            if board[0][2] != "X" and board[0][2] != "O":
                print("Computer chose 3!")
                board[0][2] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "4":
            if board[1][0] != "X" and board[1][0] != "O":
                print("Computer chose 4!")
                board[1][0] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "5":
            draw_move(board)
            
        elif comp_move == "6":
            if board[1][2] != "X" and board[1][2] != "O":
                print("Computer chose 6!")
                board[1][2] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "7":
            if board[2][0] != "X" and board[2][0] != "O":
                print("Computer chose 7!")
                board[2][0] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "8":
            if board[2][1] != "X" and board[2][1] != "O":
                print("Computer chose 8!")
                board[2][1] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        elif comp_move == "9":
            if board[2][2] != "X" and board[2][2] != "O":
                print("Computer chose 9!")
                board[2][2] = "X"
                print(board)
                return board
            else:
                draw_move(board)
                
        else:
            print("Error", type(comp_move))
            return
        
    except:
        print("Error 2")
        return

def make_board():
    board = [["1","2","3"],["4","X","6"],["7","8","9"]]
    return board
    
def main():
    board = make_board()
    while not victory_for(board):
        display_board(board)
        board = enter_move(board)
        display_board(board)
        if victory_for(board):
            victory_for(board)
            break
        print("Computer\'s turn!")
        board = draw_move(board)
        
        display_board(board)
        print("\n----------\n")
        if victory_for(board):
            victory_for(board)
            break
main()
    
