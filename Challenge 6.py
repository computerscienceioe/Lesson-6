
students = []
marks = []
grades = []

numberStudents = int(input("Enter the number of students who took the test: "))

for i in range(numberStudents):
  students.append(input("Student name: "))
  marks.append(int(input("Student mark: ")))

for i in range(len(marks)):
  if marks[i] >= 90 and marks[i] <= 100:
    grades.append("H1")
  elif marks[i] >= 80 and marks[i] < 90:
    grades.append("H2")
  elif marks[i] >= 70 and marks[i] < 80:
    grades.append("H3")
  elif marks[i] >= 60 and marks[i] < 70:
    grades.append("H4")
  elif marks[i] >= 50 and marks[i] < 60:
    grades.append("H5")
  elif marks[i] >= 40 and marks[i] < 50:
    grades.append("H6")
  elif marks[i] >= 30 and marks[i] < 40:
    grades.append("H7")
  elif marks[i] >= 0 and marks[i] < 30:
    grades.append("H8")

print()

sum = 0
for i in range(len(marks)):
  sum += marks[i]

print("The average grade in the class is", sum/len(marks))

lowestGrade = 100 # Set it to the highest grade possible at the start. 
for i in range(len(marks)):
  if marks[i] < lowestGrade:
    lowestGrade = marks[i]

print("The lowest grade in the class is", lowestGrade)

highestGrade = 0 # Set it to the lowest grade possible at the start. 
for i in range(len(marks)):
  if marks[i] > highestGrade:
    highestGrade = marks[i]

print("The highest grade in the class is", highestGrade)

print("Name\tMark\tGrade")
for i in range(len(marks)):
  print(students[i], "\t", marks[i], "\t\t", grades[i], sep="")
