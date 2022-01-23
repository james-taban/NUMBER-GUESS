#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from replit import clear
import random
from art import logo



def getting_value():
  score = random.randint(1,100)
  return score

def compare(user_value,initial_value):
  difference = user_value - initial_value
  if difference == 0:
    return 0
  elif difference >= 10:
    return "Too high"
  elif difference < -10:
    return "Too low"
  elif difference <= 5:
    return "You are getting close"
  elif difference > -10:
    return "You are getting close"


def play_game():
  print(logo)
  attempts = 0
  computer_guess = getting_value()
  continue_play = True
  
  print("Welcome to the Number Guessing Game!")
  print("Guess the number between 1 and 100")
  choice = input("Which difficulty do you choose: Easy or Hard\n").lower()
  if choice == "easy":
    attempts = 10
    print("You have 10 attempts remaining.")
  elif choice == "hard":
    attempts = 5
    print("You have 5 attempts remaining.")
   
  
  while continue_play:
    user_guess = int(input("Enter a number you want to guess: "))
    output = compare(user_guess,computer_guess)
    if output == 0:
      print("You have guessed the number correctly. You win")
      continue_play = False
    else:
     print(output)
     print("Guess again")
     attempts = attempts - 1
     print(f"You have {attempts} attempts remaining.")
     if attempts == 0:
      print("You have run out of attempts. Game over")
      continue_play = False


while input("Do you want to play a number guessing game? Type Yes or No\n").lower() == "yes":
  clear()
  play_game()
