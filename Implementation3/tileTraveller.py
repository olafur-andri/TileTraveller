# LINK TO GITHUB: https://github.com/olafur-andri/TileTraveller	

def get_possible_directions_and_flip(x, y):
  """
  Gets all possible directions the player can go (n/e/s/w) from x and y position
  """
  possible_directions = ""
  check_directions = ""
  can_flip = False

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
	  can_flip = True
  elif x == 2 and y == 2:
	  possible_directions = "(S)outh or (W)est."
	  check_directions = "sw"
	  can_flip = True
  elif x == 3 and y == 2:
	  possible_directions = "(N)orth or (S)outh."
	  check_directions = "ns"
	  can_flip = True
  elif x == 1 and y == 3:
	  possible_directions = "(E)ast or (S)outh."
	  check_directions = "es"
  elif x == 2 and y == 3:
	  possible_directions = "(E)ast or (W)est."
	  check_directions = "ew"
	  can_flip = True
  elif x == 3 and y == 3:
	  possible_directions = "(S)outh or (W)est."
	  check_directions = "sw"
  
  return possible_directions, check_directions, can_flip

def get_input_direction():
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

def flip_coin(coin_count):
	""" Gives the user the ability to gain a coin by pulling a lever. Returns the new coin_count """
	user_input = input("Pull a lever (y/n): ")

	if user_input.lower() == "y":
		coin_count += 1
		print("You received 1 coins, your total is now {}.".format(coin_count))

	return coin_count

def play():
	x = 1
	y = 1
	coin_count = 0

	while x != 3 or y != 1:
		possible_directions, check_directions, can_flip = get_possible_directions_and_flip(x, y)

		# Check if user can flip a coin
		if can_flip:
			coin_count = flip_coin(coin_count)

		print("You can travel: {}".format(possible_directions))

		# Wait for valid directions from user
		user_input = get_input_direction()
		while not user_input in check_directions:
			print("Not a valid direction!")
			user_input = get_input_direction()
		
		x, y = change_position(x, y, user_input)
	print("Victory!")

def main():
	game_running = True

	while game_running:
		play()
		user_input = input("Play again (y/n): ")
		game_running = (user_input.lower() == "y")
main()