import mountains

print(mountains)

print(mountains.TALLEST)

import mountains as m

print(m.TALLEST)

from mountains import TALLEST

print(TALLEST)






'''


https://en.wikipedia.org/wiki/List_of_mountains_of_New_Zealand_by_height

print(asteroids.simple_list)

alphabetical_asteroids = sorted(asteroids.simple_list)

print(f"First: {alphabetical_asteroids[0]}")
print(f"Last: {alphabetical_asteroids[-1]}")

#-----

asteroid_to_find = "doris"
found_it = False
for asteroid in alphabetical_asteroids:
    if asteroid == asteroid_to_find:
        found_it = True
if found_it:
    print(f"{asteroid_to_find} is in our list!")
else:
    print(f"{asteroid_to_find} is NOT in our list!")

#-----

if asteroid_to_find in alphabetical_asteroids:
    print(f"{asteroid_to_find} is in our list!")
else:
    print(f"{asteroid_to_find} is NOT in our list!")

# generally not the most efficient data structure for looking up data
# lists do guarantee their order tho

# if you just want to grab some info a dictionary is probably better

#introduce discover date dict
# then show list of dicts
# then show dict of dicts

# can tell them apart by [] vs {}
# BUT they are "indexed" the same. one uses a number (arrays) and ones uses whatever types the keys are (so could be int)
# 
#-----


# introduce the blah in x then x[blah]
# but also the x.get('blah') and f is None check
# special value




exit(0)











import requests

def blah(date):

    neo_data = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key=DEMO_KEY").json()

    neo_list = neo_data["near_earth_objects"][date]
    sizes = []
    for o in neo_list:
        cad = o["close_approach_data"]
        print(len(cad), cad[0]["orbiting_body"])
        size_m = o["estimated_diameter"]["meters"]
        sizes.append((size_m["estimated_diameter_min"], size_m["estimated_diameter_max"], cad[0]["relative_velocity"]["kilometers_per_second"], cad[0]["miss_distance"]["lunar"]))
        

    sizes.sort()
    for s in sizes:
        print(s)


                 


# for i in range(1, 15):
#     d = f"2020-04-{i:02}"
#     print(d)
#     blah(d)




# talk about trailing commas
'''