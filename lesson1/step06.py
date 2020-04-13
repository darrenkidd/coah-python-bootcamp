import requests

def print_todays_max_temperature_for_city():
  city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
  max_temp = city_data["days"][0]["max"] # <-- fixed bug
  if city == "Wellington":
    print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
  else:
    print(f"Hello {city}, your max temp will be {max_temp} degrees today!")

city = "Dunedin"
print_todays_max_temperature_for_city()

city = "Wellington"
print_todays_max_temperature_for_city()

city = "Kaitaia"
print_todays_max_temperature_for_city()

city = "Invercargill"
print_todays_max_temperature_for_city()
