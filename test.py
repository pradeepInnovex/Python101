print("Please Input Your Marks :\n")
mark = 0
grade = 'null'

mark = int(input())

if mark >= 85:
    grade = 'A'
elif mark >= 75:
    grade = 'B'
elif mark >= 65:
    grade = 'C'
elif mark >= 55:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is :", grade)
print("Your Mark is :", mark)


