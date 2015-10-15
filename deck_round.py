from random import shuffle 

n = int(raw_input("Please enter the number of cards:"))

def cardCycle(n):
	nlist= range(1, n+1)
	shuffle(nlist)
	hand_deck = nlist
	original = []
	original.extend(nlist)
	table_deck = []
	cycle = 0
	while True:
		while hand_deck:
			table_deck.insert(0, hand_deck.pop(0))
			if hand_deck:
				hand_deck.append(hand_deck.pop(0))
		#swap 
		hand_deck, table_deck = table_deck, hand_deck
		# print hand_deck
		#increment cycle round
		cycle += 1
		if hand_deck == original:
			break

	return cycle

print cardCycle(n)

# first: need to distribute the cards until the deck is no more
# second: deck = table deck 
# third: repeat 1 and 2 until table deck is in sorted order


