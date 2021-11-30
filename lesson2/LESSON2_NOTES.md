# Lists and Dictionaries

## Step 1

A very quick recap:

* Previously, we looked at simple lists i.e.
  ```python
  city_list = ["Dunedin", "Wellington", "Kaitaia", "Invercargill"]
  ```
* We can write this another way - which is much more useful if it's a longer list:
  ```python
  city_list = [
    "Dunedin",
    "Wellington",
    "Kaitaia",
    "Invercargill",
  ]
  ```
* Note here that there is a trailing comma on the last entry. Some languages care about these, but Python doesn't. This is quite a useful thing when you are reordering lists (as you don't have to manually remove the trailing comma from the last item in the list).

But this isn't usually how we are given a list. Often, we get them from somewhere else, and we're not entirely sure what's in them.

* Let's import a module where I've pre-prepared a list for us to use:
  ```python
  import mountains
  ```
* If we run the script, nothing happens. But if we see no errors, it means our script is able to import the module OK!
* Let's print the module to see what it is:
  ```python
  import mountains
  print(mountains)
  ```
* That's not very helpful. Usually, we want to use something _in_ the module, and don't care about the module itself.
* Let's print the pre-prepared list:
  ```python
  import mountains
  print(mountains.TALLEST)
  ```
* That's more like it! However, it is a little bit wordy. Let's try some alternatives:
  ```python
  import mountains as m
  print(m.TALLEST)

  from mountains import TALLEST
  print(TALLEST)
  ```
* Both of those print the same list that we saw before. But they are often a much more readable way to import your data. And readability is important (as discussed in previous lesson)!
* We can see in the print-out that the list uses  `[...]` square brackets on either end, and has more entries than we can manage easily. How would we find things easily in this list?

[**Step 1 - Finished Code**](./lesson2/step01.py)

## Step 2

* Let's settle on this style of importing:
  ```python
  from mountains import TALLEST
  ```
* Let's find out about this mysterious list. How do we count how many mountains we've got from tallest to shortest (inclusive)?
  ```python
  count = len(TALLEST)
  print(f"There are {count} mountains")
  ```
* (Ask me about `len()` and Python's "duck-typing" if you dare!) 
* I happen to know that this list is ordered from tallest to shortest. So if we wanted to get the name of the tallest mountain, we can do this:
  ```python
  tallest_mtn = TALLEST[0]
  print(f"Tallest mountain is {tallest_mtn}")
  ```
* Note how the _first_ item is indexed by the number `0`? This is the way most programming languages work for reasons that aren't important here.
* How would we quickly grab the shortest mountain? Well, Python has a cool trick:
  ```python
  shortest_mtn = TALLEST[-1]
  print(f"Shortest mountain is {shortest_mtn}")
  ```
* If you think of the list as a doughnut, with `0` as the first element, then working _backwards_ gets you the last element. Very cool! This is a lot simpler than doing this:
  ```python
  shortest_mtn_2 = TALLEST[len(TALLEST)-1]
  ```
* Try printing different items using different indexes. What happens if you use a number greater than the number of items in the list? What happens if you use other negative numbers?

A common problem you need to solve in programming (or data analysis in general) is to get a subset of the data. How do we get a shorter version of this list?

* We can use something called "slice notation". The general form of this is `list[start:end]` (where `end` is **not** inclusive e.g. it finishes at index `4` which is the 5th item in the list). If you don't provide the `start` or `end` value, it will use the start or end of the list, respectively.
* In other words (given we know this list is tallest to shortest mountains), to get the 5 tallest mountains, we can do this:
  ```python
  tallest_5 = TALLEST[:5]
  print(tallest_5)
  ```
* That's great! What about the shortest 3?
  ```python
  shortest_3 = TALLEST[-3:]
  print(shortest_3)
  ```
* So here we are starting at the third-last element, and then grabbing the second-last and last and stopping. So we end up with a new list of 3 items.
* What do you think happens if you use `[:]`?

What if we don't want it ordered by height/rank anymore? What if we want to order by name?

Python includes a built-in function called `sorted()`. It takes in an array, and then returns a new copy of that array which has been sorted.

* Let's try it on our list:
  ```python
  tallest_sorted_az = sorted(TALLEST)
  print(tallest_sorted_az)
  ```
* We can also combine our sorting and our slicing together:
  ```python
  first_3_reverse_alpha = sorted(TALLEST, reverse=True)[:3]
  print(first_3_reverse_alpha)
  ```
* You'll also see in this example that we have reversed the sort, so it's going from `z` to `a`.

[**Step 2 - Finished Code**](./lesson2/step02.py)

## Step 3

TBC


## Final Improvements

* Can we simplify our code any more? Can we reduce duplication of text?
* We could move the URL into a special variable as well.
