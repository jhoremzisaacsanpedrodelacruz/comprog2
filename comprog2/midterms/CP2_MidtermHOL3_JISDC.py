# --- Python Exception & Error Labs ---
# 1. Division by Zero
# 2. Invalid Integer Input
# 3. File Not Found
# 4. Index Out of Range
# 5. Key Not Found in Dictionary
# 6. Type Error in Addition
# 7. Custom Exception – Negative Number
# 8. Multiple Exceptions
# 9. Finally Block
# 10. Retry Until Valid Input
# 0. Exit

def lab_1():
    while True:
        try:
            num = int(input("Enter Numerator: "))
            den = int(input("Enter Denominator: "))
            result = num / den
            print(f"Result: {result}")
            break
        except ValueError:
            print("Error: Invalid value")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero! Please try again.")

def lab_2():
    age_list = []
    while True:
        age = input("Enter an age (or 'done' to finish): ")
        if age.lower() == "done":
            break
        try:
            age_list.append(int(age))
        except ValueError:
            print("Invalid input, skipping.")
    if age_list:
        average = sum(age_list)/len(age_list)
        print(f"Average age: {average}")
    else:
        print("No valid ages entered.")

def lab_3():
    file_name = input("Enter File name: ")
    try:
        with open(file_name, 'r') as f:
            print(f"{file_name} opened successfully.")
    except FileNotFoundError:
        print("File Not Found.. Creating new one")
        with open(file_name, 'w') as f:
            f.write("Welcome! This is a new file.\n")
        print(f"{file_name} created.")

def lab_4():
    fruits = ['apple', 'banana', 'cherry']
    try:
        index = int(input(f"Enter index (0-{len(fruits)-1}): "))
        print(f"You chose: {fruits[index]}")
    except IndexError:
        print("Error: Index out of range.")
        new_item = input("Add a new item to the list: ")
        fruits.append(new_item)
        print(f"Updated list: {fruits}")

def lab_5():
    grades_dictionary = {'Alice': 90, 'Bob': 85}
    name = input("Enter student name: ")
    try:
        print(f"Grade: {grades_dictionary[name]}")
    except KeyError:
        print("Error: Student not found.")
        grade = int(input(f"Enter grade for {name}: "))
        grades_dictionary[name] = grade
    print(f"Updated grades: {grades_dictionary}")

def lab_6():
    val1 = input("Enter first value: ")
    val2 = input("Enter second value: ")
    try:
        result = int(val1) + int(val2)
        print(f"Numeric Sum: {result}")
    except ValueError:
        print("Inputs are not both numbers.")
        print(f"Concatenated string: {val1}{val2}")

def lab_7():
    class NegativeNumberError(Exception):
        pass
    nums = input("Enter numbers separated by spaces: ").split()
    try:
        nums = [int(x) for x in nums]
        for n in nums:
            if n < 0:
                raise NegativeNumberError("Negative numbers not allowed!")
        print(f"All numbers are valid: {nums}")
    except NegativeNumberError as e:
        print(f"Error: {e}")

def lab_8():
    try:
        num = input("Enter numerator: ")
        den = input("Enter denominator: ")
        result = int(num) / int(den)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

def lab_9():
    try:
        num = int(input("Enter a number to divide 100 by: "))
        result = 100 / num
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        with open("log.txt", "a") as f:
            f.write("Program executed\n")
        print("Finally block executed: cleanup done.")

def lab_10():
    attempts = 0
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(f"You entered: {num}")
            break
        except ValueError:
            print("Invalid input, try again.")
            attempts += 1
    print(f"Invalid attempts before success: {attempts}")

lab_name = [
    "Division by Zero",
    "Invalid Integer Input",
    "File Not Found",
    "Index Out of Range",
    "Key Not Found in Dictionary",
    "Type Error in Addition",
    "Custom Exception – Negative Number",
    "Multiple Exceptions",
    "Finally Block",
    "Retry Until Valid Input",
]

def list_names():
    counter = 1
    for name in lab_name:
        print(f"[{counter}] {name}")
        counter += 1

while True:
    print("---[ Python Exception & Error Labs ]---")
    list_names()
    try:
        choice = int(input(f"Select a lab (0-{len(lab_name)}): "))
    except ValueError:
        print("Invalid choice!")
        continue
    match choice:
        case 1:
            lab_1()
        case 2:
            lab_2()
        case 3:
            lab_3()
        case 4:
            lab_4()
        case 5:
            lab_5()
        case 6:
            lab_6()
        case 7:
            lab_7()
        case 8:
            lab_8()
        case 9:
            lab_9()
        case 10:
            lab_10()
        case 0:
            print("Exiting...")
            break
        case _:
            print("Invalid choice!")