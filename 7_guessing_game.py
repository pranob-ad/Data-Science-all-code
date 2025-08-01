'''Guessing Game!!
Generate a random integer in the range (100, 500) and store it in a variable
Ask the user to guess (3 chances)
At every wrong guess provide the following clue:
1) If the guess is less than number and d1 (Euclidian distance wrt minima)
is less than d2 (Euclidian distance wrt maxima) then print guess is
below the number. Hint!! Number is towards minima.
2) If the guess is greater than number and d1 (Euclidian distance wrt minima)
is less than d2 (Euclidian distance wrt maxima) then print guess is
above the number. Hint!! Number is towards minima.
3) If the guess is greater than number and d1 (Euclidian distance wrt minima)
is greater than d2 (Euclidian distance wrt maxima) then print guess is
above the number. Hint!! Number is towards maxima.
4) If the guess is less than number and d1 (Euclidian distance wrt minima)
is greater than d2 (Euclidian distance wrt maxima) then print guess is
below the number. Hint!! Number is towards maxima.
'''
import math
import random

number = random.randint(100,500)
guess = 0
guess_lft = 3
d1 = math.sqrt((number**2)-(100**2))
d2 = math.sqrt((500**2)-(number**2))

while guess_lft > 0:
  guess = int(input("Enter your guess"))
  guess_lft -= 1

  if guess == number:
    print("Hurray!!! You guessed it right")
    break
  elif (guess < number) and (d1 < d2):
    print("Your guess is below the number\n")
    print("Hint!! Number is towards minima")
  elif (guess > number) and (d1 < d2):
    print("Your guess is above the number\n")
    print("Hint!! Number is towards minima")
  elif (guess > number) and (d1 > d2):
    print("Your guess is above the number\n")
    print("Hint!! Number is towards maxima")
  elif (guess < number) and (d1 > d2):
    print("Your guess is below the number\n")
    print("Hint!! Number is towards maxima")

if guess != number:
  print("You lost the game, the number is: ", number)