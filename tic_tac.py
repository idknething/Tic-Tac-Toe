#python script for Tic-Tac-Toe
#define board as 3x3 array
board = [[[] for col in range(0, 3)] for row in range(0, 3)]

#Initialize values 1-9 for board spaces:
def initialize_board():
	n = 1
	for row in range(len(board)):
		for col in range(len(board[row])):
			board[row][col] = str(n)
			n += 1

#function to print board:
def print_board():
	i = 0
	for row in board:
		print('   |   |')
		print(' {} | {} | {} '.format(row[0], row[1], row[2]))
		if (i < 2):
			print('___|___|___')
		else:
			print('   |   |')
		i += 1

#function to check player inputs:
def check_input(p_input):
	for row in board:
		if p_input in row:
			return True
	else:
		return False

#function to test win condition:
def check_win(player_turn):
	for i in range(len(board)):
		#check row wins:
		if board[i][0] == player_turn and board[i][1] == player_turn and board[i][2] == player_turn:
			print('{} wins!'.format(player_turn))
			return True
		#check col wins:
		if board[0][i] == player_turn and board[1][i] == player_turn and board[2][i] == player_turn:
			print('{} wins!'.format(player_turn))
			return True
	#check wins along two diagonals:
	if (board[0][0] == player_turn and board[1][1] == player_turn and board[2][2] == player_turn) or (board[0][2] == player_turn and board[1][1] == player_turn and board [2][0] == player_turn):
		print('{} wins!'.format(player_turn))
		return True
	#if there is no win, return false
	return False

#function to update board with player move
def make_move(p_input, turn):
	for row in range(len(board)):
		for col in range(len(board)):
			if p_input == board[row][col]:
				board[row][col] = turn
	print_board() 

#define a main game function to manage sub-fuctions and game tasks:
def play_game():

	#initial board state
	initialize_board()
	player_turn = 'X'
	#game introduction message:
	print('Welcome to Tic-Tac-Toe. X goes first.\n')
	print_board()

	num_moves = 0
	#start game loop
	while (num_moves < 9):
		#get player move
		player_input = -1
		while(check_input(player_input) == False):
			player_input = input('Enter a number 1-9 matching an empty space on the board to make a move. ')

		#make a move
		make_move(player_input, player_turn)
		#check for win
		if check_win(player_turn):
			break
		#change from X turn to O turn or O turn to X turn:
		if player_turn == 'X':
			player_turn = 'O'
		elif player_turn == 'O':
			player_turn = 'X'
		#increment move counter
		num_moves += 1
	if num_moves == 9:
		print('Tie game!')

play_game()