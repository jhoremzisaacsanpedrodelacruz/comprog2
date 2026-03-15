#JHOREMZ ISAAC DELA CRUZ
#HOL1
#JAN 17, 2026

RUNNING = True



choices = [
    "Goodbye!",
    "Assigning Functions to Variables",
    "Passing Functions as Arguments",
    "Returning Functions From Other Functions",
    "Storing Functions in Data Structures",
    "Function in a List"
]


def choice():
    pass
def menu():
    print(f"[Select Option]")
    print(f"0. {choices[0]}")
    print(f"1. {choices[1]}")
    print(f"2. {choices[2]}")
    print(f"3. {choices[3]}")
    print(f"4. {choices[4]}")
    print(f"5. {choices[5]}")
    choice = int(input("Enter your choice: "))

    return choice

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

    # Getting the inner function

    func = func1("Hello, World!")

    print(func())

def choice_4():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    # Storing functions in a dictionary

    d = {

        "add": add,

        "subtract": subtract
    }

    print(d["add"](5, 3))

    print(d["subtract"](5, 3))

def choice_5():
    def func1(msg):
        return f"Hello, {msg}!"
    def func2():
        return f"GOODBYE!"
    l = [
        func1("Jhoremz"),
        func2()
    ]

    print(l[0])
    print(l[1])
def start():
    while RUNNING:
        menu_choice = menu()
        if menu_choice == 1:
            choice_1()
        if menu_choice == 2:
            choice_2()
        if menu_choice == 3:
            choice_3()
        if menu_choice == 4:
            choice_4()
        if menu_choice == 5:
            choice_5()
        if menu_choice == 0:
            print("[Goodbye!]")
            break


start()

