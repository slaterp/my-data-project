import requests
import json
import time

# 22-round seasons
seasons_22 = [1990,1993,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

# 23-round seasons
season_23= [2012,2013,2014,2015,2016,2017,2018,2019,2021,2022]

# 24-round seasons
seasons_24 = [1991,1992,1994,2011]

# 18-round seasons (COVID-affected 2020 season)
seasons_18 = [2020]

# Enter contact email in User-Agent
headers = {'User-Agent': 'your@email.com', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

for i in range(1990, 2023):
    if i in seasons_22:
        api_url = "https://api.squiggle.com.au/?q=standings&year=" + str(i) + "&round=22"
    
    elif i in season_23:
        api_url = "https://api.squiggle.com.au/?q=standings&year=" + str(i) + "&round=23"
    
    elif i in seasons_24:
        api_url = api_url = "https://api.squiggle.com.au/?q=standings&year=" + str(i) + "&round=24"
    
    elif i in seasons_18:
        api_url = api_url = "https://api.squiggle.com.au/?q=standings&year=" + str(i) + "&round=18"
    

    response = requests.get(api_url, headers=headers)
    
    if "warning" in response.json():
        print("Warning was found! Please set UserAgent correctly.")
        break
        
    
    with open(str(i) + "_season.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
    
    # Delays api requests so Squiggle servers are not overloaded
    time.sleep(3)