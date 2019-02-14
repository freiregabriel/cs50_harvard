students = []
for i in range(3):
    name = input("Name: ")
    dorm = input("Dorm: ")
    students.append({
        "name": name,
        "dorm": dorm
    })

print(students)

for student in students:
    print(f"{student['name']} is in dorm {student['dorm']}")
# below is the same
for student in students:
    name, dorm = student.items()
    print(f"{name[1]} is in dorm {dorm[1]}")