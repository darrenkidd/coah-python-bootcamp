import requests
 
def print_todays_max_temperature_for(city):
  city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
  max_temp = city_data["days"][0]["max"]
  if city == "Wellington":
    print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
  else:
    print(f"Hello {city}, your max temp will be {max_temp} degrees today!")

city_list = ["Dunedin", "Wellington", "Kaitaia", "Invercargill"]
for city in city_list:
  print_todays_max_temperature_for(city)
