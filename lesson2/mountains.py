import csv

TALLEST = None
TALLEST_DICT = None

# https://en.wikipedia.org/wiki/List_of_mountains_of_New_Zealand_by_height

with open("nz_tallest_mountains.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    raw_list = list(reader)
    TALLEST = [m["summit"] for m in raw_list]
    TALLEST_DICT = {
        m["summit"]: {
            "rank": m["rank"],
            "stats": {
                "height_m": m["height_m"],
                "year_first_ascent": m["year_first_ascent"]
            }
        } for m in raw_list
    }
