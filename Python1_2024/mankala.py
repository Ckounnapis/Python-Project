#Charalampos Kounnapis AM:5401

def initialize_board():
	return{
		"X": 0,"Y": 0,
		"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4,
		"1": 4, "2": 4, "3": 4, "4": 4, "5": 4, "6": 4,
	}
	
def print_board(board): 
    print("+--<<--+--<<--+--<<--+-PlayerY-<<-+--<<-+-<<--+")
    print(f"| Y |6   |5   |4   |3   |2   |1   |  X  |")
    print(f"Y   | {board['6']}  | {board['5']}  | {board['4']}  | {board['3']}  | {board['2']}  | {board['1']}  |     X")
    print("B   |    |    |    |    |    |    |     B")
    print(f"A {board['X']} +----+----+----+----+----+----+  {board['Y']}  A")
    print("N   |A   |B   |C   |D   |E   |F   |     N")
    print(f"K   | {board['A']}  | {board['B']}  | {board['C']}  | {board['D']}  | {board['E']}  | {board['F']}  |     K")
    print("|   |    |    |    |    |    |    |     |")
    print("+-->>--+-->>--+-->>--+-PlayerX->>---->>-+->>--+")
	
def valid_move(player, board):
    while True:
        move = input(f"Player {player}, choose move: ").upper()
        if player == "X" and move in "ABCDEF" and board[move] >0:
            return move
        elif player == "Y" and move in "123456" and board[move] >0:
            return move
        else:
            print("Invalid move, pleas enter a valide move!")

def get_seeds(start, player, board):
	seeds = board[start]
	board[start] = 0
	current = start
	while seeds >0:
		current = next_hole(current,player)
		board[current] += 1
		seeds -= 1
	return current

def next_hole(hole, player):
    if player == "X":
        order = "ABCDEFY123456X"
    else:
        order = "123456XABCDEFY"
    indx = order.index(hole)
    return order[(indx + 1) % len(order)]

def check_end(board):
    x_empty = all(board[hole] == 0 for hole in "ABCDEF")
    y_empty = all(board[hole] == 0 for hole in "123456")
    if x_empty or y_empty:
        return True
    else: 
        return False
        
def remaining_seeds(board):
    for hole in "ABCDEF":
        board["X"] += board[hole]
        board[hole] = 0
    for hole in "123456":
        board["Y"] += board[hole]
        board[hole] = 0
        
def mankala():
    board = initialize_board()
    player = "X"
    while True:
        print_board(board)
        if check_end(board):
            remaining_seeds(board)
            print_board(board)
            if board["X"] > board["Y"]:
                print("~Player X Wins!!~")
            elif board["Y"] < board["X"]:
                print("~Player Y Wins!!~")
            else:
                print("Its a draw :)")
            break
        move = valid_move(player, board)
        last_hole = get_seeds(move, player, board)
        if last_hole == "X" or last_hole == "Y":
            continue
        if player == "Y":
            player = "X"
        else:
            player = "Y"   

mankala()