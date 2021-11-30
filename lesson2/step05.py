from mountains import TALLEST_DICT

print(TALLEST_DICT)
print(TALLEST_DICT["Mount Alarm"])

# how would we get the height?

print(TALLEST_DICT["Mount Alarm"]["stats"]["height_m"])

# if you care about order, but don't need to find something quickly, use a list
# if you care about finding it quickly, but don't care about order

# if you don't care about order, and don't care about finding it quickly, you can use either


# what happens if you do this?

# Traceback (most recent call last):
#   File "main.py", line 20, in <module>
#     print(TALLEST_DICT["Mount Kosciuszko"])
# KeyError: 'Mount Kosciuszko'

print(TALLEST_DICT["Mount Kosciuszko"])

we get a keyerror. So how do we check if it's there? one easy way is to use our helpful "in" operator

if "Mount Kosciuszko" in TALLEST_DICT:
    print("in dict")
else:
    print("not in dict")

Can also do:

mtk = TALLEST_DICT.get("Mount Kosciuszko")
print(mtk)

default is none, but you can provide a default too
mtk = TALLEST_DICT.get("Mount Kosciuszko", "")
print(mtk)



# introduce the blah in x then x[blah]
# but also the x.get('blah') and f is None check
# special value



# can we write a function to get the height of a mountain given it's name?







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






# import requests

# def blah(date):

#     neo_data = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key=DEMO_KEY").json()

#     neo_list = neo_data["near_earth_objects"][date]
#     sizes = []
#     for o in neo_list:
#         cad = o["close_approach_data"]
#         print(len(cad), cad[0]["orbiting_body"])
#         size_m = o["estimated_diameter"]["meters"]
#         sizes.append((size_m["estimated_diameter_min"], size_m["estimated_diameter_max"], cad[0]["relative_velocity"]["kilometers_per_second"], cad[0]["miss_distance"]["lunar"]))
        

#     sizes.sort()
#     for s in sizes:
#         print(s)


                 


# for i in range(1, 15):
#     d = f"2020-04-{i:02}"
#     print(d)
#     blah(d)




# talk about trailing commas

