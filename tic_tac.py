#python script for Tic-Tac-Toe
#import random to enable weak AI behavior
import random as r
#define board as 3x3 array
board = ([[[] for col in range(0, 3)] for row in range(0, 3)])

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

#function to have weak AI generate random move:
def ai_move():
	movelist = []
	#flatten board array
	for row in board:
		for val in row:
			if val != 'X' and val != 'O':
				movelist.append(val)
	return r.choice(movelist)

#function to check player move inputs:
def check_move(p_input):
	for row in board:
		if p_input in row:
			return True
	else:
		return False

#function to print menu
def print_menu(menu):
	for item in menu:
		print(menu[item])

#function to check player menu inputs:
def check_input(p_input, menu):
	if p_input in menu:
		return True
	else:
		return False

#function to test win condition:
def check_win(player_turn):
	for i in range(len(board)):
		#check row wins:
		if board[i][0] == board[i][1] == board[i][2] == player_turn:
			print('\n{} wins!'.format(player_turn))
			return True
		#check col wins:
		if board[0][i] == board[1][i] == board[2][i] == player_turn:
			print('\n{} wins!'.format(player_turn))
			return True
	#check wins along two diagonals:
	if (board[0][0] == board[1][1] == board[2][2] == player_turn) or (board[0][2] == board[1][1] == board [2][0] == player_turn):
		print('\n{} wins!'.format(player_turn))
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

#define a game function to manage sub-fuctions and game tasks:
def play_game(ai_enabled):

	#initial board state
	initialize_board()
	player_turn = 'X'
	#game introduction message:
	print_board()

	num_moves = 0
	#start game loop
	while (num_moves < 9):
		#get player move
		print("\nIt's {}'s turn.\n".format(player_turn))
		player_input = -1
		if player_turn == 'X' or ai_enabled == False:
			while(check_move(player_input) == False):
				player_input = input('Enter a number matching an empty space on the board to make a move. \n')
		#if player 2 is computer, make computer move
		elif ai_enabled == True:
			player_input = ai_move()
		

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

#define a main function to handle menus outside of game:
def main():

	play = False
	ai_player = False
	#user choice to play 2 player or against AI
	menu_one = {'1': '1 - 1 Player Game', '2': '2 - 2 Player Game', '3': '3 - Exit Game'}
	print('Welcome to Tic Tac Toe.  Please choose one of the options below:')
	print_menu(menu_one)
	menu_one_input = input('\n')
	while (check_input(menu_one_input, menu_one) == False):
		menu_one_input = input('Enter a number 1-3 from the menu above: ')

	if menu_one_input == '1':
		ai_player = True
		play = True
		print('The computer will play as O')
	elif menu_one_input == '2':
		play = True
	else:
		print('Goodbye.')

	#enable a loop to keep players in the game:
	while (play == True):
		
		play_game(ai_player)

		menu_two = {'1': '1 - Play again', '2': '2 - Exit Game'}
		print('\nWould you like to play again?\n')
		print_menu(menu_two)
		menu_two_input = input('\n')
		while (check_input(menu_two_input, menu_two) == False):
			menu_two_input = input('Enter a number 1 or 2 from the menu above: ')

		if menu_two_input == '2':
			play = False
			print('Goodbye.')
#execute game
main()