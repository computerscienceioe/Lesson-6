from random import randint

randomNumber = randint(0,20)

for i in range(5):
  guess = int(input("Guess a number between 0 and 20: "))
  if guess == randomNumber:
    print("Congratulations you have guessed correctly!")
  elif guess > randomNumber:
    print("Your guess is too high")
  elif guess < randomNumber:
    print("Your guess is too low")
print("You've had your five guesses! Did you get it right?")
