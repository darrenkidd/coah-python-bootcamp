city = "Wellington"

import requests
city_data = requests.get(f"http://metservice.com/publicData/localForecast{city}").json()

print(city_data)

# if city == "Wellington":
#   print(f"Hello beautiful {city}!")
# else:
#   print(f"Hello {city}!")
