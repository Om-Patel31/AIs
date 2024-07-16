#print("Enter everything in lowercase.")
print("Enter everything in lowercase.")

students_list = []
student_number = int(input("How many students do you have in your class? "))

for i in range(student_number):
    student_name = input("Enter the name of the student: ").strip().lower()
    students_list.append(student_name)

presence = {}
print("How it works: Write 'yes', 'no', 'late' or 'sick' to save the student's presence in the classroom.")
print()

print("Attendance:")
def take_attendance():
    for student in students_list:
        while True:
            student_presence = input(f"Is {student} there? ").strip().lower()
            if student_presence == "yes":
                presence[student] = "Present"
                break
            elif student_presence == "no":
                presence[student] = "Absent"
                break
            elif student_presence == "sick":
                presence[student] = "Sick Leave"
                break
            else:
                print("Invalid Input. Please write 'yes', 'no', or 'sick'.")

def late():
    student = input("Which student's attendance do you want to change to 'Late'? ").strip().lower()
    if student in students_list:
        presence[student] = "Late"
    else:
        print(f"{student} is not in the student list.")

    print("\nUpdated Attendance Summary:")
    for student, status in presence.items():
        print(f"→ {student}: {status}")

def main():
    take_attendance()

    print("\nAttendance Summary:")
    for student, status in presence.items():
        print(f"→ {student}: {status}")

    while True:
        change_status = input("\nDo you want to change any student's status to 'Late'? (yes/no): ").strip().lower()
        if change_status == "yes":
            late()
        elif change_status == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

main()