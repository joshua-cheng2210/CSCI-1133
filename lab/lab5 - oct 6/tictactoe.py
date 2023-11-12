import random
def print_board(board):
    i = 0
    while (i < len(board)):
        # print(i)
        if i % 3 == 0:
            print()
        print(board[i], end = "")
        i += 1
    print()
        
# print_board(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'])

def open_spots(board):
    new_list = []
    for i in range(len(board)):
        # print(i)
        if board[i] == "-":
            new_list.append(i)
    return(new_list)
            
# open_spots(['-', '-', '-', '-', '-', '-', '-', '-', '-'])

def random_move(board, symbol):
    board[random.choice(open_spots(board))] = symbol
    print_board(board)

# board = ['X', '-', 'O', '-', 'X', '-', 'X', '-', 'O']
# random_move(board, 'X')

def check_three(board,idx1,idx2,idx3):
    if board[idx1] == board[idx2] and board[idx3] == board[idx2]:
        return board[idx1]
    # elif board[idx1] and board[idx2] and board[idx3] == "O":
    #     return "O"
    else:
        return "-"

# print(check_three(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'], 1, 4, 7))
# print(check_three(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'], 2, 5, 8))
# print(check_three(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'], 0, 5, 6))
# print(check_three(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'], 2, 3, 8))

def winner(board):
    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
    for triple in combos:
        if (check_three(board, triple[0], triple[1], triple[2]) == "X"):
            return "X"
        elif (check_three(board, triple[0], triple[1], triple[2]) == "O"):
            return "O"
    if len(open_spots(board)) == 0:   
        return "D"
    return "-"

# def winner(board):
#     combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
#     while(len(open_spots(board)) != 0):
#         for triple in combos:
#             if (check_three(board, triple[0], triple[1], triple[2]) == "X"):
#                 return "X"
#             elif (check_three(board, triple[0], triple[1], triple[2]) == "O"):
#                 return "O"
#             else:
#                 "-"
#     if(len(open_spots(board)) == 0):
#         for triple in combos:
#             if (check_three(board, triple[0], triple[1], triple[2]) == "X"):
#                 return "X"
#             elif (check_three(board, triple[0], triple[1], triple[2]) == "O"):
#                 return "O"
#             else:   
#                 return "D"


# print(winner(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']))
# print(winner(['X', '-', 'O', 'X', 'O', '-', 'O', '-', 'X']))
# print(winner(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']))
# print(winner(['X', 'X', 'O', '-', 'X', '-', 'X', 'O', 'O']))
# print(winner(['-', '-', '-', 'X', 'X', 'X', 'O', 'O', '-']))

def tic_tac_toe():
    field = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    choose = ["X", "O"]
    while(winner(field) != "X" and winner(field) != "O"):
        random_move(field, choose[random.randint(0, 1)])
    return winner(field)

# print(tic_tac_toe())

def games(counter):
    test = 0
    xxx = 0
    OOO = 0
    DDD = 0
    for i in range(counter):
        test = tic_tac_toe()
        if test == "X":
            xxx += 1
        elif test == "O":
            OOO += 1
        elif test == "D":
            DDD += 1
    print(f"X wins: {xxx} ; {xxx /counter * 100}")
    print(f"O wins: {OOO} ; {OOO / counter * 100}")
    print(f"Draws: {DDD} ; {DDD / counter * 100}")

games(100)