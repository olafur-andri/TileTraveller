"""
	1. Which implementation was easier and why?

Naturally, the second implementation was easier because I used functions to divide
the problem into smaller problems which is way easier than just dealing with one
big problem. The main body of the program also became way more comprehensible so
debugging it if things didn't go correctly was simpler.

	2. Which implementation is more readable and why?

The second implemenation is more readable because the function names and the docstrings
provided for each function describes better what it is that the program does, rather
than having comments all over the place. The latter code is more "broken up" than the
former and is more readable as a consequence of that.

	3. Which problems in the first implementations were you able to solve with the latter
     implementation?

The only problems that we fixed in the latter code was that we made the code more
readable and comprehensible. I think that the way that me and my group laid out
the algorithm for this problem gave us a comprehensible way to write the code, even
if it was without functions. Using functions was, though, a lot better, no question.
"""

def get_possible_directions(x, y):
  """
  Gets all possible directions the player can go (n/e/s/w) from x and y position
  """
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
  """
    Gets the input (n/s/e/w) from the user
  """
  user_input = input("Direction: ")
  return user_input.lower()

def change_position(x, y, user_input):
  """
    Changes the current position, based on the original position and the input from the user
  """
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