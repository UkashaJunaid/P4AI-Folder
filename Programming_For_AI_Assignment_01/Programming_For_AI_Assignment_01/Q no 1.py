students = []
subjects = ["Python", "Artificial Intelligence", "Mathematics"]


def calculate_result(marks):
    total = sum(marks)
    percentage = total / 300 * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


for i in range(5):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = []

    for subject in subjects:
        mark = float(input("Enter marks in " + subject + " (out of 100): "))
        marks.append(mark)

    students.append({
        "name": name,
        "roll_number": roll_number,
        "marks": marks
    })

results = []
for student in students:
    total, percentage, grade = calculate_result(student["marks"])
    results.append({
        "name": student["name"],
        "roll_number": student["roll_number"],
        "marks": student["marks"],
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

print("\nSTUDENT RESULTS")
for result in results:
    print("\nName:", result["name"])
    print("Roll number:", result["roll_number"])
    print("Marks:", result["marks"])
    print("Total:", result["total"], "/ 300")
    print("Percentage:", round(result["percentage"], 2), "%")
    print("Grade:", result["grade"])

top_student = max(results, key=lambda item: item["percentage"])
print("\nHighest percentage:", top_student["name"])
print("Percentage:", round(top_student["percentage"], 2), "%")

with open("results.txt", "w", encoding="utf-8") as file:
    file.write("STUDENT RESULTS\n")
    for result in results:
        file.write("\nName: " + result["name"] + "\n")
        file.write("Roll number: " + result["roll_number"] + "\n")
        file.write("Marks: " + str(result["marks"]) + "\n")
        file.write("Total: " + str(result["total"]) + " / 300\n")
        file.write("Percentage: " + str(round(result["percentage"], 2)) + "%\n")
        file.write("Grade: " + result["grade"] + "\n")

    file.write("\nHighest percentage: " + top_student["name"] + "\n")
    file.write("Percentage: " + str(round(top_student["percentage"], 2)) + "%\n")

print("\nResults saved in results.txt")
