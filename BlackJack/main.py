
from art import logo
import os

def deal_card():
  '''
  deals cards from the deck: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  '''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  import random
  
  return random.choice(cards)

def calculate_score(player_cards):
  '''
  Calculates the total of the playeror computer
  1. returns 0 if player has black jack
  2. returns total of players cards
  '''
  if sum(player_cards) == 21 and len(player_cards) == 2:
    return 0
  
  if sum(player_cards) > 21 and 11 in player_cards:
    player_cards.remove(11)
    player_cards.append(1)
    
  return sum( player_cards)

def compare(player_total, cpu_total):
  '''
  Compares the user and cpu total
  '''
  if player_total == cpu_total:
    return "Draw!!"
  elif cpu_total == 0:
    return "CPU Won"
  elif player_total == 0:
    return "You Win\n"
  elif player_total == 21:
    return "You Win\n"
  elif cpu_total == 21:
    return "You Lose\n"
  elif cpu_total > player_total and cpu_total < 22:
    return "You Lose\n"
  else:
    return "You Win\n"

def play():
  '''
  Plays a game of black jack
  '''
  print(logo)
  user_cards = []
  computer_cards = []
  game_ended = False
  
  for _ in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_ended:
    user_total = calculate_score(user_cards)
    computer_total = calculate_score(computer_cards)
    
    print(f"your cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if not user_total or not computer_total or user_total > 21:
      game_ended = True
  
    if not game_ended:
      deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if deal_another_card == "y":
        user_cards.append(deal_card())
      else:
        game_ended = True
        
  while computer_total < 17 and computer_total != 0 :
    computer_cards.append(deal_card())
    computer_total = calculate_score(computer_cards)
    
  print(f"\nThe computers final hand {computer_cards} and total: {computer_total}")
  print(f"Your final hand {user_cards} and your total: {user_total}")
  print(compare(player_total = user_total, cpu_total = computer_total))
  
while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == "y":
  os.system('clear')
  play()  