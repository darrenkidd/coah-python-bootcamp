from mountains import TALLEST

def is_a_tall_mountain(mountain_to_find):
    found_mountain = None
    for mountain in TALLEST:
        if mountain_to_find.lower() in mountain.lower():
            found_mountain = mountain
    return found_mountain

my_mountain = is_a_tall_mountain("cook")
if my_mountain:
    print(f"{my_mountain} IS in our list!")
else:
    print(f"Your mountain IS NOT in our list!")
