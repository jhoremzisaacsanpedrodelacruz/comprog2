# Name : Jhoremz Isaac S. Dela Cruz
# Date : JANUARY 24, 2026
# Course: BSCS
# Year : 1
# Filename: CP2_PrelimHOL4_JISDC
# Description : 

import array as arr 

arr1 = arr.array("i", [1, 3, 5, 3, 7, 1, 9, 3])
arr2 = arr.array("i", [1, 3, 5, 3, 7, 1, 9, 3])
print(f"Original array: {arr1}")


print(f"Reverse the order of the items:")

arr1.reverse()
print(f"{arr1}")
print(f"Reverse the order of the items using negative indexing:")
print(f"{arr2[::-1]}")
input()
