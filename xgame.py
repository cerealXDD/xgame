#!/usr/bin/env python3
while(True):
	try:
		rows = int(input("Enter rows: "))
		if(rows <= 2):
			raise ValueError()
		break
	except ValueError:
		print("enter integer greater than 2")


while(True):
	try:
		columns = int(input("Enter columns: "))
		if(columns <= 2):
			raise ValueError()
		break
	except ValueError:
		print("enter integer greater than 2")


while(True):
	try:
		num_players = int(input("Enter number of players: "))
		if(num_players < 1):
			raise ValueError()
		break
	except ValueError:
		print("enter integer greater than 0")


players = []
for i in range(0, num_players):
	while(True):
		player_name = input(f"Enter name for player {i+1}: ")
		if(' ' not in player_name):
			break
		else:
			print("Please enter name without spaces")
	players.append([player_name, 0])

game_array = [['O' for _ in range(columns)] for _ in range(rows)]

# Print the initialized 2D array
def print_game_array():
	board_str = ' '*(len(str(rows)) + len(str(columns)))
	for idx in range(1, columns):
		board_str = board_str + f"{idx}" + ' '*(len(str(columns)) - len(str(idx+1)) + 1)
	board_str += f"{columns}\n"
	for row in range(1, rows + 1):
		for column in range(0, columns + 1):
			if(column == 0):
				board_str = board_str + ' '*(len(str(rows)) - len(str(row))) + str(row) + ' '*(len(str(columns)))
			else:
				board_str = board_str + game_array[row-1][column-1] + ' '*(len(str(columns)))
		board_str += "\n"
	print(board_str[:-1])

def move(row, column):
	game_array[row][column] = 'X'

def score(row, column):
	score_tmp = 0

#	print(game_array_val(row, column) + game_array_val(row-1, column) + game_array_val(row-2, column))
#	print(game_array_val(row-1, column) + game_array_val(row, column) + game_array_val(row+1, column))
#	print(game_array_val(row, column) + game_array_val(row+1, column) + game_array_val(row+2, column))
#	print(game_array_val(row, column) + game_array_val(row-1, column-1) + game_array_val(row-2, column-2))
#	print(game_array_val(row-1, column-1) + game_array_val(row, column) + game_array_val(row+1, column+1))
#	print(game_array_val(row, column) + game_array_val(row+1, column+1) + game_array_val(row+2, column+2))
#	print(game_array_val(row, column) + game_array_val(row-1, column+1) + game_array_val(row-2, column+2))
#	print(game_array_val(row-1, column+1) + game_array_val(row, column) + game_array_val(row+1, column-1))
#	print(game_array_val(row, column) + game_array_val(row+1, column-1) + game_array_val(row+2, column-2))
#	print(game_array_val(row, column) + game_array_val(row, column-1) + game_array_val(row, column-2))
#	print(game_array_val(row, column-1) + game_array_val(row, column) + game_array_val(row, column+1))
#	print(game_array_val(row, column) + game_array_val(row, column+1) + game_array_val(row, column+2))


	if(game_array_val(row, column) + game_array_val(row-1, column) + game_array_val(row-2, column) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row-1, column) + game_array_val(row, column) + game_array_val(row+1, column) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row+1, column) + game_array_val(row+2, column) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row-1, column-1) + game_array_val(row-2, column-2) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row-1, column-1) + game_array_val(row, column) + game_array_val(row+1, column+1) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row+1, column+1) + game_array_val(row+2, column+2) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row-1, column+1) + game_array_val(row-2, column+2) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row-1, column+1) + game_array_val(row, column) + game_array_val(row+1, column-1) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row+1, column-1) + game_array_val(row+2, column-2) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row, column-1) + game_array_val(row, column-2) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column-1) + game_array_val(row, column) + game_array_val(row, column+1) == 'XXX'):
		score_tmp += 1
	if(game_array_val(row, column) + game_array_val(row, column+1) + game_array_val(row, column+2) == 'XXX'):
		score_tmp += 1
	players[player_idx][1] = players[player_idx][1] + score_tmp
	return score_tmp


def game_array_val(row, column):
	if(row >= 0 and row < rows and column >=0 and column < columns):
		return game_array[row][column]
	else:
		return ''


player_idx = 0
moves = 0


while(True):
	if(moves == rows*columns):
		print("Game Over!")
		for player in sorted(players, key=lambda x: x[1], reverse=True):
			print(player[0] + ' ' + str(player[1]))
		break
	user_input = input("xgame>").split()
	if(len(user_input) == 0):
		pass
	elif(user_input[0] == 'p'):
		if(len(user_input) == 1):
			for idx,player in enumerate(players):
				player_str = player[0] + ' ' + str(player[1])
				if(player_idx == idx):
					player_str = player_str + ' (Your Turn)'
				print(player_str)
		elif(len(user_input) == 2):
			player_str = ''
			for idx,player in enumerate(players):
				if(player[0] == user_input[1]):
					player_str = player[0] + ' ' + str(player[1])
					if(player_idx == idx):
						player_str = player_str + ' (Your Turn)'
					print(player_str)
					break
			if(player_str == ''):
				print(f"{user_input[1]} not a player")
		else:
			print("p takes 0 or 1 args")
	elif(user_input[0] == 'b'):
		if(len(user_input) == 1):
			print_game_array()
		else:
			print("b takes 0 args")
	elif(user_input[0] == 'm'):
		move_error = False
		if(not move_error):
			if(len(user_input) != 3):
				print("Enter 2 args for m")
				move_error = True
		if(not move_error):
			try:
				user_input[1] = int(user_input[1])
				if(user_input[1] < 1 or user_input[1] > rows):
					raise ValueError()
				user_input[1] = user_input[1] - 1
			except ValueError:
				print(f"enter row between 1 and {rows}")
				move_error = True
			try:
				user_input[2] = int(user_input[2])
				if(user_input[2] < 1 or user_input[2] > columns):
					raise ValueError()
				user_input[2] = user_input[2] - 1
			except ValueError:
				print(f"enter column between 1 and {columns}")
				move_error = True
		if(not move_error):
			if(game_array[user_input[1]][user_input[2]] == 'X'):
				print(f"row {user_input[1] + 1} and column {user_input[2] + 1} is taken already")
				move_error = True
		if(not move_error):
			game_array[user_input[1]][user_input[2]] = 'X'
			move_score = score(user_input[1], user_input[2])
			if move_score > 0:
				print(f"+{move_score} for {players[player_idx][0]}")
			player_idx = (player_idx + 1) % num_players
			moves = moves + 1
	elif(user_input[0] == '?' or user_input[0] == 'h' or user_input[0] == 'help'):
		if(len(user_input) == 1):
			print(f"?/h/help - prints help\nb - prints board\np/p <name> - prints player info\nm <row> <column> - puts x")
		else:
			print("help takes 0 args")
	else:
		print("not a command")

