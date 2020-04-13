import requests

city = "Dunedin"
city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
max_temp = city_data["days"][1]["max"]
if city == "Wellington":
  print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
else:
  print(f"Hello {city}, your max temp will be {max_temp} degrees today!")

city = "Wellington"
city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
max_temp = city_data["days"][1]["max"]
if city == "Wellington":
  print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
else:
  print(f"Hello {city}, your max temp will be {max_temp} degrees today!")

city = "Kaitaia"
city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
max_temp = city_data["days"][1]["max"]
if city == "Wellington":
  print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
else:
  print(f"Hello {city}, your max temp will be {max_temp} degrees today!")

city = "Invercargill"
city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()
max_temp = city_data["days"][1]["max"]
if city == "Wellington":
  print(f"Hello beautiful {city}, your max temp will be {max_temp} degrees today!")
else:
  print(f"Hello {city}, your max temp will be {max_temp} degrees today!")
