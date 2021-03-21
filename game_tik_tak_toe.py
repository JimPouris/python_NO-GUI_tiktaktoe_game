#Tik Tak Toe
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1=''
p2=''
win=False
#Display the board

def display_board(board=board):
	print(f'       {board[7]}|{board[8]}|{board[9]}')
	print('      -------')
	print(f'       {board[4]}|{board[5]}|{board[6]}')
	print('      -------')
	print(f'       {board[1]}|{board[2]}|{board[3]}')

#Accept User Input

def user_input():
	while True:
		p1= input('Choose X or O: ')
		if p1.upper() not in ['X','O']:
			print('\n'*100)
		else:
			break
	if p1.upper()=='X':
		p2='O'
	else:
		p2='X'
	return p1.upper(),p2
# player_marks=user_input()
# p1=player_marks[0]
# p2=player_marks[1]

#Board Placement

def board_placement(board=board,win=win):
	while not win:
		who_won = win_argument(board)
		if who_won==True:
			print('PLAYER 1(X) WON!')
			win=True
			break
		elif who_won==False:
			print('PLAYER 2(O) WON!')
			win=True
			break
		if win==True:
			break
		elif ' ' not in board:
			break
		display_board()
		p2_placement=input('Choose where to place your marker: ')
		if p2_placement.isalpha() or int(p2_placement) not in range(1,10):
			print('\n'*100)
		else:
			if board[int(p2_placement)]==' ':
				board[int(p2_placement)]=p2
				display_board()
				p1_placement=input('Choose where to place your marker: ')
				if p1_placement.isalpha() or int(p1_placement) not in range(1,10):
					print('\n'*100)
				else:
					if board[int(p1_placement)]==' ':
						board[int(p1_placement)]=p1
					else:
						display_board()
						print('Not valid field')
			else:
				display_board()
				print('Not valid field')
	return board
# new_board = board_placement()

#See who won

def win_argument(b):
	if (b[1]==b[2]==b[3])=='X' or (b[4]==b[5]==b[6])=='X' or (b[7]==b[8]==b[9])=='X' or (b[1]==b[4]==b[7])=='X' or (b[2]==b[5]==b[8])=='X' or (b[3]==b[6]==b[9])=='X' or (b[1]==b[5]==b[9])=='X' or (b[3]==b[5]==b[7])=='X':
		return True
	elif (b[1]==b[2]==b[3])=='O' or (b[4]==b[5]==b[6])=='O' or (b[7]==b[8]==b[9])=='O' or (b[1]==b[4]==b[7])=='O' or (b[2]==b[5]==b[8])=='O' or (b[3]==b[6]==b[9])=='O' or (b[1]==b[5]==b[9])=='O' or (b[3]==b[5]==b[7])=='O':
		return False
	return None

#Start the game

def game_on(win=win):
	while not win:
		new_board=board_placement()
		if win==False:
			print('No one won :(')
			win=True

#Initiate the program

player_marks=user_input()
p1=player_marks[0]
p2=player_marks[1]

game_on()
