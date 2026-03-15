#JHOREMZ ISAAC DELA CRUZ
#HOL7
#JAN 31, 2026

fruits = ["apple","banana","cherry","mango"]

userFruitInput = input("Enter a fruit to insert: ")
userIndexInput = int(input("Enter the index to insert at: "))
userRemoveInput = input("Enter a fruit to remove: ")

fruits.insert(userIndexInput, userFruitInput)
fruits.remove(userRemoveInput)

for fruit in fruits:
    print(fruit)