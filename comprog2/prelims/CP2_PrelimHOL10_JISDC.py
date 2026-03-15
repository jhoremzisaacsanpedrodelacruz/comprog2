#JHOREMZ ISAAC S. DELA CRUZ
#FEB 7, 2026
#CP2_PrelimHOL9_JISDC.py

RUNNING = True

while RUNNING:
    even = []
    odd = []

    userInput = input("Enter list of integer, [separate by space]:")
    userInput.strip()

    numbers = list(map(int, userInput.split()))

    for number in numbers:
        if number%2 == 0:
            even.append(number)
        else:
            odd.append(number)            

    total = sum(numbers)   
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")

