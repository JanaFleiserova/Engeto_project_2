"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
author: Jana Fleišerová
email: fleiserova.jana@gmail.com
discord: Jana F.
"""

from random import sample
from time import time

separator = "-----------------------------------------------"
guess = 0

def adjust_sample():
      while True:
            number = sample(range(10), 4)
            if number[0] != 0:
                  break
      return number

def compare(number, guess_number):
      bull = 0
      cow = 0
      for i in range(4):
            if str(number[i]) == guess_number[i]:
                  bull += 1
            elif str(number[i]) in guess_number:
                  cow += 1
      return bull, cow

def find_time(start_time, end_time):
      time_sec = end_time - start_time
      minutes = int(time_sec / 60)
      seconds = round(time_sec - int(minutes) * 60)
      return minutes, seconds

def add_s_if_plural(word, quantity):
      if quantity == 1:
            return word
      elif quantity != 1 and word[-1] == "s":
            return word + "es"
      else:
            return word + "s"


print(f"Hi there!\n"
      f"{separator}\n"
      f"I've generated a random 4 digit number for you.\n"
      f"Let's play a bulls and cows game.\n"
      f"{separator}\n")

number = adjust_sample()
start_time = time()

while True:
      guess_number = input("Enter a number: ")

      if not guess_number.isdigit():
            print(f"Invalid input. {guess_number} isn't a number.")
            print(separator)

      elif len(guess_number) != 4 or guess_number[0] == "0" or len(set(guess_number)) < 4:
            print("Invalid input. Please enter a 4-digit number with unique digits that doesn't begin with '0'.")
            print(separator)

      else:
            guess += 1
            bull, cow = compare(number, guess_number)

            if bull == 4:
                  end_time = time()
                  minutes, seconds = find_time(start_time, end_time)

                  print(f"Correct, you've guessed the right number in "
                        f"{minutes} "
                        f"{add_s_if_plural('minute', minutes)} and "
                        f"{seconds} "
                        f"{add_s_if_plural('second', seconds)} "
                        f"in {guess} {add_s_if_plural('guess', guess)}!")

                  break
            else:
                  print(f"{bull} {add_s_if_plural('bull', bull)}, "
                        f"{cow} {add_s_if_plural('cow', cow)}")
                  print(separator)




