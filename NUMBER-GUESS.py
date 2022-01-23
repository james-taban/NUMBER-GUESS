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
  list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

  score = random.choice(list_numbers)
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
     attempts = attempts - 1
     print(f"You have {attempts} attempts remaining.")
     if attempts == 0:
      print("You have run out of attempts. Game over")
      continue_play = False


while input("Do you want to play a number guessing game? Type Yes or No\n").lower() == "yes":
  clear()
  play_game()
