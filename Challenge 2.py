
print("You are in with a chance to win a \nfree ticket to a mystery location!")
letter = input("Enter a, b, or c to be in with \na chance of winning!")

if letter == "a" or letter == "A":
  print("You have won a free ticket to Dundrum Shopping Center")
elif letter == "b" or letter == "B":
  print("You have won a free ticket to Tallaght")
elif letter == "c" or letter == "C":
  print("You have won a free ticket to Broombridge")
else:
  print("Invalid entry, \"", letter, "\" was not an option!", sep="")
