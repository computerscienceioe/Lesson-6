
from random import randint

player = input("Please choose rock(r), paper(p) or scissors(s): ")

print()
print("Player chose", player)

options = ["r","p","s"]
computer = options[randint(0,2)]

print("Computer chose", computer)

if player == computer:
  print("DRAW!")
elif player == "r" and computer == "s":
  print("Player wins!")
elif player == "r" and computer == "p":
  print("Computer wins!")
elif player == "p" and computer == "s":
  print("Computer wins!")
elif player == "p" and computer == "r":
  print("Player wins!")
elif player == "s" and computer == "p":
  print("Player wins!")
elif player == "s" and computer == "r":
  print("Computer wins!")
else:
  print("Somethings gone wrong! Try running the program again.")
