#JHOREMZ ISAAC S. DELA CRUZ
#FEB 7, 2026
#CP2_PrelimHOL9_JISDC.py

RUNNING = True

while RUNNING:
    userInput = input("Enter list of integer, [separate by space]:")
    userInput.strip()

    numbers = list(map(int, userInput.split()))

    total = sum(numbers)   
    print(f"The sum of the list is: {total}")
