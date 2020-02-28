#!/usr/bin/env python3

import random

class invalid_player:
  """Raised whenever function arguments refer to a non-existant player."""
  pass

class invalid_draw:
  """Raised when a draw is attempted on an empty deck."""
  pass

class card:
  
  def __init__(self, suit, number, value): #If ace causes an overflow, subtract the total value by 10.
    self.suit = suit
    self.number = number
    self.value = value
  
  def show_card(self):
    print(self.number," of ",self.suit)


'''
class chips:

    def __init__(self, no_chips):
      self.value = value

'''
    
class deck:
  #Implement a transfer function to player.  
  def __init__(self, no_decks):
    self.cards = []
    number_array = ["Joker", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Jack", "Queen", "King", "Ace"]
    suit_array = ["Spades", "Hearts", " Clubs", "Diamonds"]
    for i in range(len(suit_array)):
      for j in range(len(number_array)):
        cur_card = card(suit_array[i], number_array[j], j + 1)
        self.cards.append(cur_card)
    
  def add_card(self, card):
    self.cards.append(card)
    
  def show_deck(self):
    for i in range(len(self.cards)):
      self.cards[i].show_card()

  def pop_top(self):
    return self.cards.pop()

  def shuffle(self):
    random.shuffle(self.cards)
  def size(self):
    return len(self.cards)

#Add a player class
class player:
  def __init__(self, hand):
    self.hand = hand
    self.value = 0
    self.numChips = 0
  def show_hand(self):
    for i in range(len(self.hand)):
      self.hand[i].show_card()
  def return_value(self):
    self.value = 0
    for i in range(len(self.hand)):
      self.value += self.hand[i].value
    return self.value
  def add_to_hand(self, card):
    self.hand.append(card)


class state:

  def __init__(self, no_players):
    self.no_players = no_players
    self.pool = deck(1) #1 is hardcoded for MVP. Can be easily changed later.
    self.players = []
    for i in range(no_players):
      self.players.append(player([]))

  def show_board(self):
    for i in range(self.no_players):
      self.players[i].show_hand()
      print(self.players[i].return_value())

  def give_card(self, player_index):
    try:
      if(self.pool.size() <= 0):
        raise invalid_draw
      if(player_index > self.no_players):
        raise invalid_player

      self.players[player_index].add_to_hand(self.pool.pop_top())

    except invalid_draw:
        print("There are no more cards in the deck.")
    except invalid_player:
        print("The targeted player does not exist.")

  def initialize(self):
    self.pool.shuffle()
    for x in range(2):
      for i in range(self.no_players):
        self.give_card(i)



#Add a state class
#Contains all of this information packaged within a single class.
#Create an array of players, with 0 being the dealer.
#There should be one deck with the appropriate amount of cards.
#Constructor argument should specifcy player count. (2 for MVP).

#test_state = state(4)
#test_state.initialize()
#test_state.show_board()
