from mountains import TALLEST

mountain_to_find = "Aoraki (Mount Cook)"
found_it = False

# do this bit second
if mountain_to_find in TALLEST:
    found_it = True

if found_it:
    print(f"{mountain_to_find} IS in our list!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")




# then just
if mountain_to_find in TALLEST:
    print(f"{mountain_to_find} IS in our list!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")


# then
mountain_to_find = "Egmont"

found_it = False
for mountain in TALLEST:
    if mountain_to_find in mountain:
        found_it = True

if found_it:
    print(f"{mountain_to_find} IS in our list!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")


# exercise - get the full name of the mountain!
found_mountain = None
for mountain in TALLEST:
    if mountain_to_find in mountain:
        found_mountain = mountain

if found_mountain:
    print(f"{mountain_to_find} IS in our list as {found_mountain}!")
else:
    print(f"{mountain_to_find} IS NOT in our list!")


'''



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