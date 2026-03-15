# Name : Jhoremz Isaac S. Dela Cruz
# Date : FEB 13, 2025
# Course: BSCS
# Year : 1
# Filename: CP2_Prelim_JISDC_MINIPROJ.py
# Description : Compilation of Prelim Laboratory exercises 

import array as arr


# ------------------ PRELIM LAB 1 ------------------

def prelim_lab_1():
    choices = [
        "Goodbye!",
        "Assigning Functions to Variables",
        "Passing Functions as Arguments",
        "Returning Functions From Other Functions",
        "Storing Functions in Data Structures",
        "Function in a List"
    ]

    def menu():
        print("\n[Select Option]")
        for i, choice in enumerate(choices):
            print(f"{i}. {choice}")
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            return -1

    def choice_1():
        def msg(name):
            return f"Hello, {name}!"
        f = msg
        print(f("Jhoremz"))

    def choice_2():
        def msg(name):
            return f"Hello {name}."
        def func1(fun2, name):
            return fun2(name)
        print(func1(msg, "Jhoremz"))

    def choice_3():
        def func1(msg):
            def func2():
                return f"Message: {msg}"
            return func2
        func = func1("Hello, World!")
        print(func())

    def choice_4():
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        d = {"add": add, "subtract": subtract}
        print(d["add"](5, 3))
        print(d["subtract"](5, 3))

    def choice_5():
        def func1(msg):
            return f"Hello, {msg}!"
        def func2():
            return "GOODBYE!"
        l = [func1("Jhoremz"), func2()]
        print(l[0])
        print(l[1])

    while True:
        menu_choice = menu()

        if menu_choice == 1:
            choice_1()
        elif menu_choice == 2:
            choice_2()
        elif menu_choice == 3:
            choice_3()
        elif menu_choice == 4:
            choice_4()
        elif menu_choice == 5:
            choice_5()
        elif menu_choice == 0:
            print("[Goodbye!]")
            break
        else:
            print("Invalid choice!")


# ------------------ PRELIM LAB 2 ------------------

def prelim_lab_2():
    arr1 = arr.array("i", [1, 3, 5, 7, 9])
    for i in arr1:
        print(i)

    print("Access first three items individually:")
    print(arr1[0])
    print(arr1[1])
    print(arr1[2])
    input("Press Enter to continue...")


# ------------------ PRELIM LAB 3 ------------------

def prelim_lab_3():
    arr1 = arr.array("i", [1, 3, 5, 7, 9])
    print(f"Original array: {arr1}")

    arr1.append(11)
    print(f"After appending 11: {arr1}")
    input("Press Enter to continue...")


# ------------------ PRELIM LAB 4 ------------------

def prelim_lab_4():
    arr1 = arr.array("i", [1, 3, 5, 3, 7, 1, 9, 3])
    arr2 = arr.array("i", [1, 3, 5, 3, 7, 1, 9, 3])

    print(f"Original array: {arr1}")
    arr1.reverse()
    print(f"Reversed using reverse(): {arr1}")
    print(f"Reversed using slicing: {arr2[::-1]}")
    input("Press Enter to continue...")


# ------------------ PRELIM LAB 5 ------------------

def prelim_lab_5():
    arr1 = arr.array("i", [1, 2, 3, 1, 2, 5])
    print(arr1)

    found_3 = 3 in arr1
    found_6 = 6 in arr1

    print("Item 3 found" if found_3 else "3 Not found")
    print("Item 6 found" if found_6 else "6 Not found")

    input("Press Enter to continue...")


# ------------------ PRELIM LAB 6 ------------------

def prelim_lab_6():
    arr1 = arr.array("i", [1, 3, 5, 3, 7, 9, 3])
    print(f"Original array: {arr1}")
    print(f"Occurrences of 3: {arr1.count(3)}")
    input("Press Enter to continue...")


# ------------------ PRELIM LAB 7 ------------------

def prelim_lab_7():
    numbers = []
    for i in range(5):
        while True:
            try:
                userInput = int(input("Enter an integer: "))
                numbers.append(userInput)
                break
            except ValueError:
                print("Invalid input!")

    print("Your list:", *numbers)
    input("Press Enter to continue...")


# ------------------ PRELIM LAB 8 ------------------

def prelim_lab_8():
    fruits = ["apple", "banana", "cherry", "mango"]

    userFruitInput = input("Enter a fruit to insert: ")
    userIndexInput = int(input("Enter the index to insert at: "))
    userRemoveInput = input("Enter a fruit to remove: ")

    fruits.insert(userIndexInput, userFruitInput)

    if userRemoveInput in fruits:
        fruits.remove(userRemoveInput)

    for fruit in fruits:
        print(fruit)

    input("Press Enter to continue...")


# ------------------ PRELIM LAB 9 ------------------

def prelim_lab_9():
    while True:
        userInput = input("Enter list of integers (separate by space): ").strip()
        try:
            numbers = list(map(int, userInput.split()))
        except ValueError:
            print("Invalid input!")
            continue

        print(f"The sum of the list is: {sum(numbers)}")

        if input("Try again? (y/n): ").lower() != "y":
            break


# ------------------ PRELIM LAB 10 ------------------

def prelim_lab_10():
    while True:
        even = []
        odd = []

        userInput = input("Enter list of integers (separate by space): ").strip()

        try:
            numbers = list(map(int, userInput.split()))
        except ValueError:
            print("Invalid input!")
            continue

        for number in numbers:
            (even if number % 2 == 0 else odd).append(number)

        print(f"Even numbers: {even}")
        print(f"Odd numbers: {odd}")

        if input("Try again? (y/n): ").lower() != "y":
            break


# ------------------ MAIN MENU ------------------

while True:
    print("\nMAIN MENU:")
    print("[1] Preliminary Laboratory")
    print("[X] Exit Program")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        while True:
            print("\n--[[Preliminary Laboratory Exercises]]--")
            for i in range(1, 11):
                print(f"[{i}] Lab Exer {i}")
            print("[B] Back To Main Menu")

            prelim_choice = input("Enter your choice: ")

            labs = {
                "1": prelim_lab_1,
                "2": prelim_lab_2,
                "3": prelim_lab_3,
                "4": prelim_lab_4,
                "5": prelim_lab_5,
                "6": prelim_lab_6,
                "7": prelim_lab_7,
                "8": prelim_lab_8,
                "9": prelim_lab_9,
                "10": prelim_lab_10,
            }

            if prelim_choice in labs:
                labs[prelim_choice]()
            elif prelim_choice.lower() == "b":
                break
            else:
                print("Invalid Choice!")

    elif main_choice.lower() == "x":
        break
    else:
        print("Invalid Choice!")
