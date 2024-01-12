#!/usr/bin/env python3
while(True):
	try:
		rows = int(input("Enter rows: "))
		if(rows <= 0):
			raise ValueError()
		break
	except ValueError:
		print("enter integer greater than 0")


while(True):
	try:
		columns = int(input("Enter columns: "))
		if(columns <= 0):
			raise ValueError()
		break
	except ValueError:
		print("enter integer greater than 0")


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
	for row in game_array:
		print(row)

def move(row, column):
	game_array[row][column] = 'X'


player_idx = 0


while(True):
	user_input = input("xgame>").split()
	if(len(user_input) == 0):
		pass
	elif(user_input[0] == 'p'):
		for idx,player in enumerate(players):
			str = player[0] + ' ' + str(player[1])
			if(player_idx == idx):
				str = str + ' (Your Turn)'
			print(str)
	elif(user_input[0] == 'b'):
		print_game_array()
	elif(user_input[0] == 'm'):
		move_error = False
		if(not move_error):
			if(len(user_input) != 3):
				print("Enter 2 args for m")
				move_error = True
		if(not move_error):
			try:
				user_input[1] = int(user_input[1])
				if(user_input[1] < 0 or user_input[1] >= rows):
					raise ValueError()
			except ValueError:
				print(f"enter row between 0 and {rows-1}")
				move_error = True
			try:
				user_input[2] = int(user_input[2])
				if(user_input[2] < 0 or user_input[2] >= columns):
					raise ValueError()
			except ValueError:
				print(f"enter column between 0 and {columns-1}")
				move_error = True
		if(not move_error):
			if(game_array[user_input[1]][user_input[2]] == 'X'):
				print(f"row {user_input[1]} and column {user_input[2]} is taken already")
				move_error = True
		if(not move_error):
			game_array[user_input[1]][user_input[2]] = 'X'
			player_idx = (player_idx + 1) % num_players
	else:
		print("not a command")

