# https://en.wikipedia.org/wiki/List_of_mountains_of_New_Zealand_by_height

import csv

TALLEST = None
TALLEST_DICT = None

with open("nz_tallest_mountains.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    TALLEST_DICT = list(reader)
    TALLEST = [m["summit"] for m in TALLEST_DICT]
