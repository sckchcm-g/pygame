import random

number = random.randint(0, 9)
guess = int(input("Guess a number between 0 and 9: "))

while guess != number:
  if guess < number:
    print("Guess higher")
  else:
    print("Guess lower")
  guess = int(input("Guess again: "))

print("Congratulations! You guessed the number correctly")