import requests
from bs4 import BeautifulSoup
import pandas as pd

# Add User-Agent to your request, some site do not response to the request which dnose not has User-Agent
#header = {"User-Agent":"Chrome/81.0.4044.129 Safari/537.36"} in request.get(url, headers=header)

header = {'Accept-Language': 'en-US,en;q=0.8'}
request_page = requests.get(
    "https://www.timeanddate.com/weather/",headers=header
)

soup = BeautifulSoup(request_page.content,'html.parser')
content = soup.find('table',class_='zebra fw tb-theme')

all_place_in_page = content.find_all('a') 
all_temp_in_page = content.find_all('td',class_='rbi')
all_day_in_page = content.find_all('td',class_='r')

all_place = [ name.get_text().strip() for name in all_place_in_page ]
all_temp = [ (name.get_text()).replace('xa',' ') for name in all_temp_in_page ]
all_day = [name.get_text().strip() for name in all_day_in_page if name.get_text() != '']

data = pd.DataFrame(
    {
        'place' : all_place,
        'day' : all_day,
        'weather' : all_temp,
    }
)
print(data)
data.to_csv("world_weather.csv")
