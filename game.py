#!/usr/bin/env python3
###
###
###
###


##TODO: Move existing functions into classes


import sys
from objects import state

def game():

  keepPlaying = True
  playerWins = 0
  dealerWins = 0

  #numPlayers = input("How many players? ")
  numPlayers = 1
  numPlayers+=1 
  ## add 1 player for dealer (dealer is players[0])
  
  ##start game with 500 chips
  chipCount = 500


  firstRound = True

  while(keepPlaying):
    

    dealerBust = False
    playerBust = False

    dealerBlackjack = False
    playerBlackjack = False
    
    game_state = state(numPlayers)
    game_state.initialize()

    game_state.players[1].numChips = chipCount
 
    print("\nYou currently have ", chipCount, " chips")

    betAmount = chipCount * 2 
    while(betAmount > chipCount):
      betAmount = input("How many chips would you like to bet?")
      if(betAmount.isDigit() == False):
          print("\nPlease enter a valid number!")
      else:
          betAmount = int(betAmount)
          if(betAmount > chipCount):
            print("\You dont have that many chips!")

    print("\nYour cards: ")
    game_state.players[1].show_hand()
    print(game_state.players[1].return_value())

    print("\nDealer is showing: ")
    game_state.players[0].hand[0].show_card()

    dealerBust = checkBust(game_state, "dealer")
    playerBust = checkBust(game_state, "player")
    
    dealerBlackjack = checkBlackjack(game_state, "dealer")
    playerBlackjack = checkBlackjack(game_state, "player")    

    while (dealerBust == False and playerBust == False and playerBlackjack == False and dealerBlackjack == False):
      
      user_decision(game_state)

      dealerBust = checkBust(game_state, "dealer")
      playerBust = checkBust(game_state, "player")
      
      dealerBlackjack = checkBlackjack(game_state, "dealer")
      playerBlackjack = checkBlackjack(game_state, "player")

      numDealerHand = len(game_state.players[0].hand)
      
      print("\nYour cards: ")
      game_state.players[1].show_hand()
      print(game_state.players[1].return_value())

      print("\nDealer is showing: ")
      for i in range(numDealerHand-1):
        game_state.players[0].hand[i].show_card()


    print("\nGame over. Your cards: ")
    game_state.players[1].show_hand()
    print(game_state.players[1].return_value())
    
    print("\nDealer cards: ")
    game_state.players[0].show_hand()
    print(game_state.players[0].return_value())

    result = score(game_state)
    if result == 1:
      playerWins+=1
    else:
      dealerWins+=1

    play_again(dealerWins, playerWins)



def user_decision(game_state):
  choice = input("\nHit, Stand, or Double down? H/S/D ").upper()
  if choice == 'H':
    hit(game_state, "playerHit")
  elif choice == 'S':
    hit(game_state, "dealerHit")
  elif choice == 'D':
    doubleDown(game_state, player[1])



def checkBlackjack(game_state, player):
  if player == "player":
    if game_state.players[1].return_value() == 21:
      return(True)
    else:
      return(False)

  elif player == "dealer":
    if game_state.players[0].return_value() == 21:
        return(True)
    else:
        return(False)
        

def checkBust(game_state, player):
  if player == "player":
    if game_state.players[1].return_value() > 21:
      return(True)
    else:
      return(False)

  elif player == "dealer":
    if game_state.players[0].return_value() > 21:
      return(True)
    else:
      return(False)    


'''
def doubleDown(game_state, player):

    game_state.give_card(1)

'''

def hit(game_state, player):

  if(player == 'playerHit'):
    game_state.give_card(1)

  elif(player == 'dealerHit'):
    game_state.give_card(0)



def score(game_state):
  
  dealer_score = game_state.players[0].return_value()
  player_score = game_state.players[1].return_value()

  if player_score == 21:
    print("\nYou got a blackjack")
    return(1)
  elif dealer_score == 21:
    print("\nThe dealer got a blackjack")
    return(0)
  elif dealer_score > 21:
    print("\nDealer busted")
    return(1)
  elif player_score > 21:
    print("\nYou busted")
    return(0)
  elif dealer_score > player_score:
    print("\nDealer has a higher score")
    return(0)
  elif player_score > dealer_score:
    print("\nYour score is higher than the dealers")
    return(1)





def play_again(dealerWins, playerWins):

  keepPlaying_input = input("\nKeep playing? (y/n) ").lower()
  if(keepPlaying_input == 'y'):
    keepPlaying = True
  else:
    keepPlaying = False

  if(keepPlaying):
      print("\n\n\t\tNEW GAME\n")
      print("-----\t-----\t-----\t-----\t-----\t-----\t\n\n\n")
  else:
    print("Dealer wins: ", dealerWins, "Your wins: ",playerWins)
    exit()



if __name__ == "__main__":
  game()
