# 1. Sum of items in a list
list1=["banana","boy","box","bag"]
print(len(list1))

#  write a function that takes in 2 lists and returns true if they have one common member
#  append a new member 55
#  replace a member

def has_similar_member(list_a, list_b):
    # Check if there is at least one common member between the two lists
    for item in list_a:
        if item in list_b:
            return True
    return False

def append_member(my_list, new_member):
    # Append a new member to the list
    my_list.append(new_member)

def replace_member(my_list, old_member, new_member):
    # Replace a specific member in the list with a new member
    if old_member in my_list:
        index = my_list.index(old_member)
        my_list[index] = new_member


list_a = [6,8,10]
list_b = [7,9,11]

# Check if the two lists have a common member
common_member = has_similar_member(list_a, list_b)
print("Do the two lists have a common member?", common_member)

# Append a new member (55) to one of the lists
append_member(list_a, 55)

# Replace a member (4) with a new member (44) in one of the lists
replace_member(list_b, 9,15)

print("Modified list_a:", list_a)
print("Modified list_b:", list_b)
