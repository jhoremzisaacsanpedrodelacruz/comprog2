
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
# Select a lab (0-10):


def lab_1():
    while True:
        try:
            num = int(input("Enter Numerator: "))
            den = int(input("Enter Denominator: "))
            result = num/den
            print(f"Result: {result}")
            break
        except ValueError:
            print("Error: Invalid value")
            continue
        except ZeroDivisionError:
            print("Error: Cannot divide by zero! Please try again.")
            continue


def lab_2():
    while True:

        age_list = []

        while True:
            try:
                age = input("Enter an age (or 'done' to finish): ")
                
                if age == "done":
                    break
            except ValueError:
                print("Error: Invalid input, skipping.")
                continue
            except ZeroDivisionError:
                print("Error: Cannot divide by zero! Please try again.")
                break
            else:
                try:
                    age_list.append(int(age))
                except ValueError:
                    print("Error: Invalid input, skipping.")
                    continue
        result = sum(age_list)/len(age_list)
        print(f"Average age: {result}")
        break

def lab_3():
    try:
        file_name = input("Enter File name: ")
        open(f"{file_name}", 'r')
    except FileNotFoundError:
        print("File Not Found.. Creating new one")
        open(f"{file_name}", "w")

def lab_4():
    try:
        fruits = ['apple', 'banana', 'cherry']
        choice = int(input("Enter Index (0-2): "))
        print(f"You chose: {fruits[choice]} ")
    except IndexError:
        print("Error: Index out of range.")

def lab_5():
    try:
        grades_dictionary = {
            'Alice':90, 
            'Bob':85
            }

        name = input("Enter student name: ")
        print(f"Grade: {grades_dictionary[name]}")


        
    except KeyError:
        print("Error: Student not found.")
        new_grade =  int(input(f"Enter grade for {name}: "))
        grades_dictionary[name] = new_grade
    print(f"Update grades: {grades_dictionary}")

def lab_6():
    pass    

def lab_7():
    pass

def lab_8():
    pass

def lab_9():
    pass

def lab_10():
    pass

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
        counter+= 1

while True:
    print("---[ Python Exception & Error Labs ]---")
    list_names()

    try:
        choice = int(input(f"Select a lab (0-{len(lab_name)}): "))
    except ValueError:
        print("invalid choice!")
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
