students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        usn = input("Enter USN: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[usn] = {
            "Name": name,
            "Marks": marks
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for usn, details in students.items():
                print(f"USN: {usn}")
                print(f"Name: {details['Name']}")
                print(f"Marks: {details['Marks']}")
                print("----------------------")

    elif choice == "3":
        search_usn = input("Enter USN to search: ")

        if search_usn in students:
            print("\nStudent Found!")
            print("Name:", students[search_usn]["Name"])
            print("Marks:", students[search_usn]["Marks"])
        else:
            print("Student not found.")

    elif choice == "4":
        delete_usn = input("Enter USN to delete: ")

        if delete_usn in students:
            del students[delete_usn]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")