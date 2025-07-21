student_marks = \
    {
    "Alice": 85,
    "Dev": 90,
    "Chandu": 78,
    "Benu":98,
    "Evan":78
    }
name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
