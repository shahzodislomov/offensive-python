score = int(input("Enter your score: "))
grade = ''
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(f"Your grade is: {grade}")

