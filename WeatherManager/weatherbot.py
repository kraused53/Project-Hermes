from OPEN_WEATHER_KEYS import OPEN_WEATHER_API_KEY
from requests import get, exceptions
from datetime import datetime


# ----------------------------------------------------------------------------
"""
    Use the requests library to make an API call to Open Weather. If the 
        request is successful, return the requestd data as a JSON data set.
        If the request fails, return None data type. The None response is to
        be handled by the caller of the function
"""
def get_weather_json(lat = '40.7128', lon = '-74.0030', exclusions = ''):

    API_URL = 'https://api.openweathermap.org/data/2.5/onecall?' +\
        'lat=' + str(lat) + '&lon=' + str(lon) +\
        '&exclude=' + exclusions +\
        '&units=imperial' +\
        '&appid=' + OPEN_WEATHER_API_KEY

#    print(API_URL)

    try:
        response = get(API_URL)
    except exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    
    # Check to make sure response.get() worked
    if response is not None:
        # Check for valid response
        if response.status_code == 200:
            return response.json()
        else:
            return None