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
