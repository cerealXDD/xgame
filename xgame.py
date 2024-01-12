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

game_array = [['O' for _ in range(columns)] for _ in range(rows)]

# Print the initialized 2D array
def print_game_array():
	for row in game_array:
		print(row)

def move(row, column):
	game_array[row][column] = 'X'

print_game_array()

while(True):
	user_input = input("xgame>").split()
	if(user_input[0] == 'p'):
		print_game_array()
	elif(user_input[0] == 'm'):
		if(len(user_input) == 3):
			try:
				user_input[1] = int(user_input[1])
				if(user_input[1] < 0 or user_input[1] >= rows):
					raise ValueError()
			except ValueError:
				print(f"enter row between 0 and {rows-1}")
			try:
				user_input[2] = int(user_input[2])
				if(user_input[2] < 0 or user_input[2] >= columns):
					raise ValueError()
			except ValueError:
				print(f"enter column between 0 and {columns-1}")
		else:
			print("Enter 2 args for m")

