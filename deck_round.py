import random

class Deck(object): 
	"""Represents a deck of cards"""
	#class properties
	def __init__ (self, num):
		self.cards = list(range(num))

	def shuffle(self):
		"""Shuffles the cards in this deck"""
		random.shuffle(self.cards)

	def add_card(self):
		"""Add a card to the bottom of the deck"""
		self.card.append(card)

	def remove_card(self):
		"""Remove a card from the top"""
		return self.card.pop(0)

	def move_to_table(self, table, num_cards):
		"""Move top card from top of the deck to the table"""
		for i in self.cards:
			hand.add_card(self.pop_card(0))

	def move_to_bottom (self, num_cards):
		"""Move top card to bottom of the deck"""
		for i in self.cards:
			self.cards.add_card(self.pop(0))

class Table(Deck):
	""" Represents the deck on the table"""
	def __init__ (self):
		self.cards = []


first_deck = Deck(5)
first_deck.shuffle()
print first_deck.cards