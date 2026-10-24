student = {}
while True:
    print("\n-----------STUDENT MANAGER APP-----------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    # Add students

    if choice == "1":
        name = input("Enter student name: ").strip()
        
        # check if name is digit
        if name.isdigit():
            print("Enter valid name!")
        else:
            marks = int(input("Enter marks: "))

            # check valid marks input
            if marks > 100 or marks < 0:
                print("Invalid marks!")
            else:
                student[name] = marks
                print(f"{name} Successfully Added!")  

          
    # View students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(f"{name} : {marks}")

    # Check result of any spacific student
    elif choice == "3":
        name = input("Enter student name to see result: ").strip()
        if name in student:
            marks = student[name]
            print(f"{name} : {marks}")
            if marks < 40:
                print("FAIL!")
            else:
                print("PASS")
        else:
            print("Student not found!")

    # Exit
    elif choice == "4":
        print("Exited!!!")
        break

    # Invalid choice
    else:
        print("Invalid Input!!!")