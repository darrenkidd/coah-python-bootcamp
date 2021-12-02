from mountains import TALLEST

mountain_to_find = "Aoraki (Mount Cook)"
found_it = False

for mountain in TALLEST:
    if mountain == mountain_to_find:
        found_it = True

if found_it:
    print(f"{mountain_to_find} IS in our list!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")

# ---------------------------

if mountain_to_find in TALLEST:
    print(f"{mountain_to_find} IS in our list!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")


# ---------------------------

# Challenge...

found_mountain = None
for mountain in TALLEST:
    if mountain_to_find in mountain:
        found_mountain = mountain

if found_mountain:
    print(f"{mountain_to_find} IS in our list as {found_mountain}!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")
