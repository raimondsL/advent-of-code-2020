# Advent of Code 2020
# --- Day 7: Handy Haversacks ---
import os
import re

file_name = "INPUT.txt"
my_dict = {}
my_bag = "shiny gold"
set_of_bags = set()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, file_name)

if os.path.isfile(my_file):
    file_handler = open(my_file, "r")
else:
    print(f"File not found: {my_file}")
    exit(2)

for read_line in file_handler:
    line = read_line.split(" bags contain ")
    my_dict[line[0]] = re.findall(r"\d\s(.+?)\sbag", line[1])
    
# print(my_dict)

def recursive_bag_check(bag):
    global my_dict, set_of_bags
    for k, v in my_dict.items():
        if bag in v:
            set_of_bags.add(k)
            recursive_bag_check(k)

recursive_bag_check(my_bag)

print("How many bag colors can eventually contain at least one shiny gold bag?")
print(f"Answer: {len(set_of_bags)}\n")

# --- Part Two --- (keeping part 1 as is)

my_dict.clear()

if os.path.isfile(my_file):
    file_handler = open(my_file, "r")
else:
    print(f"File not found: {my_file}")
    exit(2)

for read_line in file_handler:
    line = read_line.split(" bags contain ")
    my_dict[line[0]] = re.findall(r"(\d)\s(.+?)\sbag", line[1])

# print(my_dict)

def recursive_check_bag_count(bag):
    # shiny gold bags contain 1 muted olive bag, 5 dotted red bags, 1 drab plum bag.
    global my_dict
    count = 0
    for x in my_dict[bag]:
        dict_count = int(x[0])
        dict_bag = x[1]
        count += dict_count + dict_count * recursive_check_bag_count(dict_bag)
    return count

my_count = recursive_check_bag_count(my_bag)
print("How many individual bags are required inside your single shiny gold bag?")
print(f"Answer: {my_count}")