# Import the necessary modules
import requests
import json

# Set the URL of the API
API_KEY = "e40b0f1e-7637-403f-91c9-6816da9d9f17"
STATE_NAME = "Kerala"
COUNTRY_NAME = "India"
api_url = f"http://api.airvisual.com/v2/cities?state={STATE_NAME}&country={COUNTRY_NAME}&key={API_KEY}"

# Send a request to the API
response = requests.get(api_url)
# Store the data from API
json_data = response.json()


# Check if the request was successful
if response.status_code == 200:
    print(response.json())
    pass

else:
    # If the request failed, display an error message
    print("An error occurred: {}".format(response.status_code))

# Return JSON of city lists available in the state (To be used in the Telegram module)
def cityLists():
    city_list=json_data['data']
    ciudad=[d['city'] for d in city_list]
    return ciudad 

# Returns the AQI Level of a certain city selected by the user
def City_Stats(CITY_NAME):
  city_url = f"http://api.airvisual.com/v2/city?city={CITY_NAME}&state={STATE_NAME}&country={COUNTRY_NAME}&key={API_KEY}"
  rp = requests.get(city_url)
  data=rp.json()
  aqi = data['data']['current']['pollution']['aqius']
  return str(aqi) 