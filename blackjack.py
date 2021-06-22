import random

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __repr__(self):
		return f'{self.suit} of {self.rank}'

class Deck:
	def __init__(self):
		self.cards = [Card(r, s) for r in [1,2,3,4,5,6,7,8,9,10,11,12,13] for s in 
				["hearts", "diamonds", "clubs", "spades"]]

	def shuffle(self):
		if len(self.cards) > 1:
			random.shuffle(self.cards)

	def deal(self):
		if len(self.cards) > 1:
			return self.cards.pop(0)
	
class Player:
	def __init__(self, dealer=False):
		self.hand = []
		self.dealer = dealer
		self.rank = 0

	def hit(self, card):
		self.hand.append(card)

	def calc_total(self):
		self.rank = 0
		for card in self.hand:
			if card.rank.isnumeric():
				self.rank += int(card.rank)

	def get_total(self):
		self.calc_total()
		return self.rank

	def show_cards(self):
		if self.dealer:
			print("[X]")
			print(self.hand[1])
		else:
			for card in self.hand:
				print(card)
			print("Total: ", get_total())

class Game:
	@classmethod
	def run(self):
		print("Welcome")
		
		active = True
		while active:
			self.deck = Deck()
			self.deck.shuffle()

			self.player_cards = Player()
			self.dealer_cards = Player(dealer=True)

			for i in range(2):
				self.player_cards.hit(self.deck.deal())
				self.dealer_cards.hit(self.deck.deal())

			confirmation = input("would you like to start a new game? (y/n) ").lower()
			if confirmation == 'n':
				active = False
			elif confirmation == 'y':
				game_over = False
				print("\n[[[Dealer is shufflilng...]]")
				while not game_over:
					print("\nPlayer's hand: ")
					self.player_cards.show_cards()
					print("\nDealer's hand: ")
					self.dealer_cards.show_cards()

					choice = input("\nhit or stay? ")
					
					if choice == 'hit':  # class for hit and stay?
						self.player_cards.hit(self.deck.deal())
						if self.player_cards.get_total() > 21:
							print("you lose")
						# self.player_cards.show_cards()
					elif choice == 'stay':
						# check total player vs total dealer
						game_over = True
						# if dealer total is higher than player, dealer wins
						# if dealer total is lower than player, player wins
						# if dealer total is > 21 dealer loses
						# if player total is > 21 player loses

		print("Thanks you for playing!")

Game.run()

