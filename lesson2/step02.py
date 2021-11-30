from mountains import TALLEST

count = len(TALLEST)
print(f"There are {count} mountains")

tallest_mtn = TALLEST[0] # zero-based 
print(f"Tallest mountain is {tallest_mtn}")

shortest_mtn = TALLEST[-1]
print(f"Shortest mountain is {shortest_mtn}")

# ---------------------------

tallest_5 = TALLEST[:5]
print(tallest_5)

shortest_3 = TALLEST[-3:]
print(shortest_3)

# ---------------------------

tallest_sorted_az = sorted(TALLEST)
print(tallest_sorted_az)

first_3_reverse_alpha = sorted(TALLEST, reverse=True)[:3]
print(first_3_reverse_alpha)
