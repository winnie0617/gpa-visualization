course_info = [] # stores each course's title, credits, grade
valid_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']

# get user input
while True:
    title = input("Enter course title (enter -1 if you're done): ")
    if title == "-1":
        break

    credits = input("Enter course credits: ")
    while not credits.isdigit():
        credits = input("Invalid input! Try again...")
    credits = int(credits)

    grade = input("Enter course grade: ")
    while not grade in valid_grades:
        grade = input("Invalid input! Try again...")

    course_info.append({"title": title, "credits": credits, "grade": grade})

print(course_info)
