"""
Engeto_project_2.py: druhý projekt do Engeto Online Python Akademie
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

def convert_to_minutes(time_sec):
      minutes = time_sec / 60
      seconds = round(time_sec - int(minutes) * 60)
      return minutes, seconds

def add_s_if_plural(word, quantity):
      if quantity == 1:
            return word
      elif quantity > 1 and word[-1] == "s":
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

      elif len(guess_number) != 4 or guess_number[0] == "0" or len(set(guess_number)) < 4:
            print("Invalid input. Please enter a 4-digit number with unique digits that doesn't begin with '0'.")

      else:
            guess += 1

            bull, cow = compare(number, guess_number)

            if bull == 4:
                  end_time = time()
                  time_sec = end_time - start_time
                  minutes, seconds = convert_to_minutes(time_sec)

                  print(f"Correct, you've guessed the right number in "
                        f"{int(minutes)} "
                        f"{add_s_if_plural('minute', int(minutes))} and "
                        f"{seconds} "
                        f"{add_s_if_plural('second', seconds)} "
                        f"in {guess} {add_s_if_plural('guess', guess)}!")

                  with open("statistiky.txt", mode="r") as txt:
                        lines = txt.readlines()

                        if lines == [] or lines == ["\n"]:
                              turn = 1
                              cum_sec = time_sec
                              cum_guess = guess
                        else:
                              turn = int(lines[-5:][0][6:]) + 1
                              cum_sec = float(lines[-5:][2][13:]) + time_sec
                              cum_guess = int(lines[-5:][4][13:]) + guess

                  avg_minutes, avg_seconds = convert_to_minutes(cum_sec/turn)

                  print(f"The average guessing time is {int(avg_minutes)} "
                        f"{add_s_if_plural('minute', int(avg_minutes))} "
                        f"and {avg_seconds} "
                        f"{add_s_if_plural('second', avg_seconds)}. "
                        f"The average number of attemps is {round(cum_guess/turn)} "
                        f"{add_s_if_plural('guess', round(cum_guess/turn))}. ")

                  with open("statistiky.txt", mode="a") as txt:
                        txt.write(f"turn: {turn}\n"
                                  f"seconds: {time_sec}\n"
                                  f"cum_seconds: {cum_sec}\n"
                                  f"number of guesses: {guess}\n"
                                  f"cum_guesses: {cum_guess}\n")
                  break

            else:
                  print(f"{bull} {add_s_if_plural('bull', bull)}, {cow} {add_s_if_plural('cow', cow)}")
                  print(separator)




