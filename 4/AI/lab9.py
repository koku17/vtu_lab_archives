#!/bin/python
def print_board(board):
	for row in board:
		print(' | '.join(row))
		print('-'*9)

def check_winner(board, player):
	for row in board:
		if all(cell==player for cell in row):
			return True
	for col in range(3):
		if all(board[row][col]==player for row in range(3)):
			return True
	if all(board[i][i]==player for i in range(3)):
		return True
	if all(board[i][2-i]==player for i in range(3)):
		return True
	return False

def is_full(board):
	return all(cell!=' ' for row in board for cell in row)

def tic_tac_toe():
	board=[[' ' for _ in range(3)] for _ in range(3)]
	current_player='X'
	while True:
		print(f'Player {current_player}\'s turn :\n')
		print_board(board)
		row=int(input('\nEnter row (1-3) : '))
		col=int(input('Enter column (1-3) : '))
		print('\n')
		row-=1
		col-=1
		if board[row][col]==' ':
			board[row][col]=current_player
		else:
			print('Invalid move!\nTry again\n')
			continue
		if check_winner(board, current_player):
			print_board(board)
			print(f'\nPlayer {current_player} wins !\n')
			break
		if is_full(board):
			print_board(board)
			print('\nIt\'s a tie !\n')
			break
		current_player='O' if current_player=='X' else 'X'

if __name__=='__main__':
	tic_tac_toe()
