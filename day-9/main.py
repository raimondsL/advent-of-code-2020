# Advent of Code 2020
# --- Day 9: Encoding Error ---
import os
import re

file_name = "INPUT.txt"

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, file_name)

if os.path.isfile(my_file):
    file_handler = open(my_file, "r")
else:
    print(f"File not found: {my_file}")
    exit(2)

my_list = [int(read_line) for read_line in file_handler]

# print(my_list)

def find_invalid(slice, digit):
    for x in range(25):
        for y in range(25):
            if slice[x] != slice[y] and slice[x] + slice[y] == digit:
                # print(f"CORRECT: {slice[x]} != {slice[y]} and {slice[x]} + {slice[y]} == {digit}")
                return False
    return True

for x in range(25, len(my_list) - 1):
    if find_invalid(my_list[x - 25:x], my_list[x]):
        print("What is the first number that does not have this property?")
        invalid_number = my_list[x]
        print(f"Answer: {invalid_number}\n")
        # exit(0)
        break

# --- Part Two --- (keeping part 1 as is)

def find_end(n):
    global my_list, invalid_number
    total = 0
    for x in range(n, len(my_list) - 1):
        total += my_list[x]
        if total == invalid_number:
            return x
        if total > invalid_number:
            return 0

for x in range(len(my_list) - 1):
    y = find_end(x)
    if y != 0:
        break

# print(f"Found it: {x},{y+1}")

mi = min(my_list[x:y + 1])
ma = max(my_list[x:y + 1])
# print(f"{mi} and {ma}")
print("What is the encryption weakness in your XMAS-encrypted list of numbers?")
print(f"Answer: {mi + ma}")
