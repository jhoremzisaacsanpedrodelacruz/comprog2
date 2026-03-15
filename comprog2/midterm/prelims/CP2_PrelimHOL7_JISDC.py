#JHOREMZ ISAAC DELA CRUZ
#HOL7
#JAN 31, 2026

numbers = []

for i in range(5):
    userInput = int(input("Enter an integer:"))
    numbers.append(userInput)
    
print(f"Your list:", *numbers)