# Name : Jhoremz Isaac S. Dela Cruz
# Date : JANUARY 24, 2026
# Course: BSCS
# Year : 1
# Filename: CP2_PrelimHOL5_JISDC
# Description : 

import array as arr 

arr1 = arr.array("i", [1,2,3,1,2,5])

print(f"{arr1}")

found_3 = False
found_6 = False

for i in arr1:
    if i == 3:
        found_3 = True
    if i == 6:
        found_6 = True

if found_3:        
    print(f"Item {3} found")
else:
    print(f"{3} Not found")

if found_6:
    print(f"Item {6} found")
else:
    print(f"{6} Not found")
    


input()
