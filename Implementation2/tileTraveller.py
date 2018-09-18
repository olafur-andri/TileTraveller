"""
	1. Which implementation was easier and why?

Naturally, the second implementation was easier because I used functions to divide
the problem into smaller problems which is way easier than just dealing with one
big problem. The main body of the program also became way more comprehensible so
debugging it if things didn't go well was simpler.
"""

def get_possible_directions(x, y):
  possible_directions = ""
  check_directions = ""
  
  if x == 1 and y == 1:
	  possible_directions = "(N)orth."
	  check_directions = "n"
  elif x == 2 and y == 1:
	  possible_directions = "(N)orth."
	  check_directions = "n"
  elif x == 3 and y == 1:
	  possible_directions = "(N)orth"
	  check_directions = "n"
  elif x == 1 and y == 2:
	  possible_directions = "(N)orth or (E)ast or (S)outh."
	  check_directions = "nes"
  elif x == 2 and y == 2:
	  possible_directions = "(S)outh or (W)est."
	  check_directions = "sw"
  elif x == 3 and y == 2:
	  possible_directions = "(N)orth or (S)outh."
	  check_directions = "ns"
  elif x == 1 and y == 3:
	  possible_directions = "(E)ast or (S)outh."
	  check_directions = "es"
  elif x == 2 and y == 3:
	  possible_directions = "(E)ast or (W)est."
	  check_directions = "ew"
  elif x == 3 and y == 3:
	  possible_directions = "(S)outh or (W)est."
	  check_directions = "sw"
  
  return possible_directions, check_directions

def get_input():
  user_input = input("Direction: ")
  return user_input.lower()

def change_position(x, y, user_input):
  if user_input == "n":
	  y += 1
  elif user_input == "e":
	  x += 1
  elif user_input == "s":
	  y -= 1
  elif user_input == "w":
    x -= 1
	
  return x, y

x = 1
y = 1

while x != 3 or y != 1:
	possible_directions, check_directions = get_possible_directions(x, y)
	print("You can travel: {}".format(possible_directions))

	user_input = get_input()

	# Wait for valid directions from user
	while not user_input in check_directions:
		print("Not a valid direction!")
		user_input = get_input()
	
	x, y = change_position(x, y, user_input)
	

print("Victory!")