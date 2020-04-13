# The Basics, Weather API and Refactoring

## Step 1

Let's start with the absolute basics: printing some text to the screen.

* The `print()` command will just output text to the screen.
* You can add comments to your code using the `#` character i.e.
  ```python
  # print something
  print("something") # see, comments
  ```
* Use comments to make notes of tricky things as you go along. It helps you as
  the programmer remember what you were doing and why. Python won't execute
  these.
* In programming, _text_ is often called a _string_ (that is, a string/sequence
  of characters).
* We can change the text to something else i.e.
  ```python
  print("Hello Wellington!")
  ```
* This isn't that remarkable. If that's all we could do, it wouldn't be very
  useful. Let's make it so we can easily change some of the text.
  ```python
  city = "Wellington"
  print(f"Hello {city}!")
  ```
* Here we are saying that a variable called "city" is going to be _assigned_
  (or given) the value of "Wellington".
* What happens if we remove the `f` we added at the start? It breaks! We need
  to tell Python that this string contains a variable - the `f` tells Python
  that this string is a special _format-string_ which means it knows to look
  for things surrounded by `{}` and treat them as variables.
  * NOTE: Use `{{` to print a `{` should you ever need to.

[**Step 1 - Finished Code**](./lesson1/step01.py)

## Step 2

One of the powerful constructs available to us in programming is something
called a "conditional" i.e. if something is TRUE then do THIS, OTHERWISE do
THAT.

* Let's change the text slightly if we are talking about Wellington:
  ```python
  if city == "Wellington":
    print(f"Hello beautiful {city}!")
  else:
    print(f"Hello {city}!")
  ```
* The `==` means "equals"; this checks that something is the same as something
  else (equality check). It's different to assignment. Try removing the extra
  equals sign and see what python says.
* The error message is saying that this is incorrect syntax - you can't _assign_
  a value to something when you're doing an `if` statement.
* Python is very picky about formatting here - you must indent the extra lines.
  Try sticking all of the lines at the same level.
  ```python
  if city == "Wellington":
  print(f"Hello beautiful {city}!")
  else:
  print(f"Hello {city}!")
  ```
* It will break with an `IndentationError`. This is Python's way of making sure
  your code always looks clean and tidy (so you can read it easier).
* To make sure our logic is correct, try changing the city to Dunedin or
  Auckland. The text should change.

[**Step 2 - Finished Code**](./lesson1/step02.py)

## Step 3

We're going to show some of the potential of modern programming now... you can
pull data from other places and rearrange it or combine it with other data to do
useful work.

* We are going to connect to the MetService API which publishes key weather data
  online for us to use (sort of).
* We can check out what the MetService API data looks like by clicking on
  [this link](https://www.metservice.com/publicData/localForecastWellington). We
  are going to grab the max temperature from this data and use it in our code.
* Often you don't have the time or desire to write all of the code you need to
  do every little thing. It's generally better to see if someone else has
  already written it for you. This saves a lot of time!
* We're going to need to use a _library_ called `requests`, which allows us to
  easily make calls to other web services. We _use_ this library by calling the
  `import` statement.
  ```python
  import requests
  city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()

  print(city_data)
  ```
* This prints out the same data that we saw in the browser link above. But we
  can now work with it.

[**Step 3 - Finished Code**](./lesson1/step03.py)

## Step 4

Let's get the maximum temperature out of our blob of data.

* Don't worry too much about the magic here - we are just asking for the first
  day, and then getting the max temperature for that day.
  ```python
  max_temp = city_data["days"][1]["max"]
  print(max_temp)
  ```
* Now let's update the text we print out, and include the max temperature.
  ```python
  if city == "Wellington":
    print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
  else:
    print(f"Hello {city}, your max temp will be {max_temp} degrees today!")
  ```
* Try changing the city to Christchurch or Tauranga. The text (including max
  temperature) will change.

[**Step 4 - Finished Code**](./lesson1/step04.py)

## Step 5

What would we do if we wanted to display the max temp for 4 different cities in
one go?

* Let's copy and paste this code so that we can run it multiple times for four
  different cities (Dunedin, Wellington, Kaitaia and Invercargill).
* First we'll move our `import` statement up to the top. You typically do this
  once in your program, at the top, not multiple times nor near where it's used
  (as we've done so far for simplicity).
* If you run the code now, it should print out max temperatures for the four
  cities.

[**Step 5 - Finished Code**](./lesson1/step05.py)

## Step 6

But guess what, I just spotted a bug in my code! I've been picking the wrong numbered day out of the `city_data` blob!

* In programming, most of the time the zero'th element in a list is actually
  the first. So by asking for day `1` I'm actually grabbing the second day!
  ```python
  max_temp = city_data["days"][1]["max"]
  ```
* It needs to be changed to this...
  ```python
  max_temp = city_data["days"][0]["max"]
  ```
* Now, we could copy and paste this fix everywhere, but what if this code was
  spread across files? We've highlighted a big issue with our code: duplication!
* There has to be a better way... there is. We can _refactor_ our code into a
  separate _function_, a piece of reusable code that does something for us.
* Then we can just _call_ that function every time we want that thing done.
  * NOTE: the term _refactor_ is just a fancy way of saying _rearrange our code
    so it behaves the same overall but in a more maintainable way_. Maintability
    is a key consideration in programming!
* So Let's move our code into the function (remembering to fix the bug too).
  ```python
  def print_todays_max_temperature_for_city():
    city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
    max_temp = city_data["days"][0]["max"]
    if city == "Wellington":
      print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
    else:
      print(f"Hello {city}, your max temp will be {max_temp} degrees today!")
  ```
* Here we've defined a new function called `print_todays_max_temperature_for_city()`.
  When we call it, it will execute all of the code inside of that function block.
  It looks lke this:
  ```python
  city = "Dunedin"
  print_todays_max_temperature_for_city()

  city = "Wellington"
  print_todays_max_temperature_for_city()

  city = "Kaitaia"
  print_todays_max_temperature_for_city()

  city = "Invercargill"
  print_todays_max_temperature_for_city()
  ```
* This is a big improvement! We can even hide away the actual implementation of
  the function using code folding, and now our code is even easier to read!

[**Step 6 - Finished Code**](./lesson1/step06.py)

## Step 7

Let's try something quickly...

* What happens if we add an extra line that sets the `city` variable _inside_
  of the function?
  ```python
  def print_todays_max_temperature_for_city():
    city = "Auckland"
    city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
    max_temp = city_data["days"][0]["max"]
    if city == "Wellington":
      print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
    else:
      print(f"Hello {city}, your max temp will be {max_temp} degrees today!")
  ```
* Let's run it using `city = "Dunedin"`. What happens? Every line displays Auckland!
* Python used the value from the _local_ copy of the variable. This is all about
  scope. Everything at the top level is called _global_, and then as we define
  data within blocks, that data becomes local to the thing that encloses it.
  Let's try a quick example here:
  ```python
  if city == "Wellington":
    adjective = "beautiful"
    print(f"Hello {adjective} {city}, your max temp will be {max_temp} degrees today!")
  else:
    print(f"Hello {adjective} {city}, your max temp will be {max_temp} degrees today!")
  ```
* We get a yucky error message saying that we used the `adjective` variable
 _before_ we had told Python about it. But we _had_ told Python... just in the
  wrong block or _scope_.
* If we change it to `city = "Wellington"`, then it will work fine.
* Is there a better way for us to pass the variable from the _outer_ scope into
  the _inner_ scope of the function? Yes - We can pass _parameters_ to our
  function.
  ```python
  def print_todays_max_temperature_for_city(city):
    ...
  ```
* Here we can say that the function _takes a parameter_ called `city`. We can
  now call the function like this:
  ```python
  city = "Dunedin"
  print_todays_max_temperature_for_city(city)
  ```
* The name of the variable _outside_ of the function is unrelated to the name
  of the parameter _inside_ the function. So we can do this as well:
  ```python
  the_city_name = "Dunedin"
  print_todays_max_temperature_for_city(the_city_name)
  print_todays_max_temperature_for_city("Bluff")
  ```
* Finally, because Python is a super expressive language that lets you write
  your code to make it easy to understand, I'm going to rename the function to
  make it read well. We can also remove the `city` variables because we can just
  pass the string/text in directly.
  ```python
  def print_todays_max_temperature_for(city):
    ...
  
  print_todays_max_temperature_for("Dunedin")
  ```  
  * Do that for all four cities and it looks much nicer!

[**Step 7 - Finished Code**](./lesson1/step07.py)

## Step 8

So we've tried out two powerful programming _constructs_: conditionals and
functions. Let's introduce a new one: repetition or looping.

* First, let's create a list of our cities.
  ```python
  city_list = ["Dunedin", "Wellington", "Kaitaia", "Invercargill"]
  ```
* Lists are just comma-separated values inside of square brackets.
* Now, let's loop through each city (or item) in the list and print it out.
  ```python
  for city in city_list:
    print(city)
  ```
* This means that as our list size changes (grows or shrinks) we can dynamically
  change the number of times we call our function (which is better than our
  copy-paste approach before).
  ```python
  city_list = ["Dunedin", "Wellington", "Kaitaia", "Invercargill"]
  for city in city_list:
    print_todays_max_temperature_for(city)
  ```

[**Step 8 - Finished Code**](./lesson1/step08.py)

## Final Improvements

* Can we simplify our code any more? Can we reduce duplication of text?
* We could move the URL into a special variable as well.
