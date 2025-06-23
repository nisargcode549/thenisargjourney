# Marks Calculator
# This program calculates the total, average, and highest marks from five subjects.

a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))
d = int(input("Enter marks of subject 4: "))
e = int(input("Enter marks of subject 5: "))
f = [a, b, c, d, e]

total_marks = sum(f)
avg = total_marks / 5
highest_marks = max(f)

print(f"📊 Total: {total_marks}, Average: {avg}, Highest: {highest_marks}")
