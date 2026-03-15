# Name : Jhoremz Isaac S. Dela Cruz
# Date : OCTOBER 24, 2025
# Course: BSCS
# Year : 1
# Filename: CP1_FinalLabExer3_JISDC
# Description : Lambda Functions

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

string_menu = "--- Python Function Arguments Menu ---"
string_choices = [
    "Exit",
    "Greet",
    "Add",
    "Student Info",
    "Custom Message",
    "Rectangle Area",
    "Profile",
    "Sum All",
    "Show Details",
    "Display",
    "Order System"
]

# ========== LABS ==========

def ask_prompt(prompt, default=None):
    try:
        input_value = input(prompt)
        if input_value.strip() == "":
            return default
        return input_value
    except ValueError as e:
        print("invalid input")
        return default

def lab_1():
    """Lab 1: Greeting with Default Argument"""
    pass

def lab_2():
    """Lab 2: Calculator with Default Argument"""
    pass

def lab_3():
    """Lab 3: Student Info with Keyword Arguments"""
    pass

def lab_4():
    """Lab 4: Custom Message with Keyword Arguments"""
    pass

def lab_5():
    """Lab 5: Rectangle Area with Positional Arguments"""
    pass

def lab_6():
    """Lab 6: Mixing Positional and Keyword Arguments"""
    pass

def lab_7():
    """Lab 7: Variable-Length Positional Arguments (*args)"""
    pass

def lab_8():
    """Lab 8: Variable-Length Keyword Arguments (**kwargs)"""
    pass

def lab_9():
    """Lab 9: Combining *args and **kwargs"""
    pass

def lab_10():
    """Lab 10: Mini Project – Order System"""
    pass

# ========== MENU SYSTEM ==========

def ask():
    try:
        return int(input("Select a lab to run (0-10): "))
    except ValueError:
        print("Invalid input.")
        return -1

def menu():
    while True:
        clear()
        
        print(string_menu)
        for i in range(1, len(string_choices)):
            print(f"{i}. {string_choices[i]}")
        print("0. Exit")

        choice = ask()
        if choice == 0:
            print("Exiting... 👋")
            break

        clear()
        match choice:
            case 1: lab_1()
            case 2: lab_2()
            case 3: lab_3()
            case 4: lab_4()
            case 5: lab_5()
            case 6: lab_6()
            case 7: lab_7()
            case 8: lab_8()
            case 9: lab_9()
            case 10: lab_10()
            case _: print("Invalid choice.")
        input("\nPress Enter to continue...")

menu()
