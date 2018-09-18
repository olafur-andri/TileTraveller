"""
Algorithm:

Byrja að búa til breytur x og y sem tákna staðsetninguna á kortinu, x = 1 og y = 1

Á meðan spilari er ekki á reit 3,1:
	Ná hvaða leiðum spilarinn má fara (með if og elif)
	Skrifa út mögulegar leiðir
	Fá inntak frá spilara
	Ef spilarinn slær inn svar sem er gilt:
		Breyta x og y gildum
	Annars:
		Prenta út villumeldingu

Prenta út “Victory!”
"""

x = 1
y = 1

while x != 3 or y != 1:
	# Get all possible inputs
	print("You can travel: ", end="")
	check_directions = ""

	if x == 1 and y == 1:
		print("(N)orth.")
		check_directions = "n"
	elif x == 2 and y == 1:
		print("(N)orth.")
		check_directions = "n"
	elif x == 3 and y == 1:
		print("(N)orth")
		check_directions = "n"
	elif x == 1 and y == 2:
		print("(N)orth or (E)ast or (S)outh.")
		check_directions = "nes"
	elif x == 2 and y == 2:
		print("(S)outh or (W)est.")
		check_directions = "sw"
	elif x == 3 and y == 2:
		print("(N)orth or (S)outh.")
		check_directions = "ns"
	elif x == 1 and y == 3:
		print("(S)outh or (E)ast.")
		check_directions = "se"
	elif x == 2 and y == 3:
		print("(E)ast or (W)est.")
		check_directions = "ew"
	elif x == 3 and y == 3:
		print("(S)outh or (W)est.")
		check_directions = "sw"

	# Take input
	direction_str = input("Direction: ")
	direction_str = direction_str.lower()

	if direction_str in check_directions:
		# Change direction based on input
		
	else:
		# Incorrect input
		print("Not a valid direction!")