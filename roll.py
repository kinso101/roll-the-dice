''' this is a 
die game'''
from random import randint
from time import sleep
def get_user_guess():
  guess = int(input("guess the number"))
  return guess
def roll_dice(number_of_sides):
  first_roll=randint(1,number_of_sides)
  second_roll= randint(1,number_of_sides)
  max_val = number_of_sides*2
  print max_val
  guess = get_user_guess()
  if guess > max_val:
    print "no guessing higher than possible"
  else:
    print "rolling..."
    sleep(2)
    print "the first roll is" + str(first_roll)
    sleep(1)
    print "the second roll is" + str(second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "yAY! YOU WIN!"
    else:
      print"you are such a loser"
      
roll_dice(6)
