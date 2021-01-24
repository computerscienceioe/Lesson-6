
percentage = float(input("Enter you exam grade as a \nnumber between 0-100 : "))

if percentage >= 90 and percentage <= 100:
  grade = "H1"
elif percentage >= 80 and percentage < 90:
  grade = "H2"
elif percentage >= 70 and percentage < 80:
  grade = "H3"
elif percentage >= 60 and percentage < 70:
  grade = "H4"
elif percentage >= 50 and percentage < 60:
  grade = "H5"
elif percentage >= 40 and percentage < 50:
  grade = "H6"
elif percentage >= 30 and percentage < 40:
  grade = "H7"
elif percentage >= 0 and percentage < 30:
  grade = "H8"

print("You received the grade", grade)
