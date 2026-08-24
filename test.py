# Student Grade Calculator

students = [
    {"name": "mumtahin", "math": 85, "science": 90, "english": 78},
    {"name": "shahid", "math": 92, "science": 88, "english": 95},
    {"name": "noor", "math": 70, "science": 75, "english": 80},
    {"name": "mudassir", "math": 98, "science": 94, "english": 91},
    "name": "jahid", "math": 65, "science": 72, "english": 68}
]


def calculate_average(math, science, english):
    total = math + science + english
    average = total / 3
    return average


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print("=" * 50)
print("           STUDENT GRADE REPORT")
print("=" * 50)

total_average = 0
highest_average = 0
lowest_average = 100
best_student = ""
worst_student = ""

for student in students:
    average = calculate_average(
        student["math"],
        student["science"],
        student["english"]
    )

    grade = get_grade(average)

    total_average += average

    if average > highest_average:
        highest_average = average
        best_student = student["name"]

    if average < lowest_average:
        lowest_average = average
        worst_student = student["name"]

    print()
    print("Name:", student["name"])
    print("Math:", student["math"])
    print("Science:", student["science"])
    print("English:", student["english"])
    print("Average:", round(average, 2))
    print("Grade:", grade)

class_average = total_average / len(students)

print()
print("=" * 50)
print("SUMMARY")
print("=" * 50)

print("Number of students:", len(students))
print("Class average:", round(class_average, 2))
print("Best student:", best_student)
print("Highest average:", round(highest_average, 2))
print("Lowest student:", worst_student)
print("Lowest average:", round(lowest_average, 2))

print()
print("Program finished.")
