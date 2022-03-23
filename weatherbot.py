import OPEN_WEATHER_KEYS
from requests import get, exceptions
from datetime import datetime


# ----------------------------------------------------------------------------
"""
    Use the datetime library to convert an integer unix timestamp and a unix
        timezone offset to calculate string formated time and date.
    
    Inputs:
        dt      -> Int
                    unix time-code
        tz      -> Int
                    unix time-code timexone offset
        AM_PM   -> Bool
                    True:  Convert to 12 hour clock 
                    Flase: Convert to 24 hour clock
    Output:
        Returns given time data as a formated string
"""
def convert_time(dt, tz, AM_PM):
    if not isinstance(dt, int):
        dt = int(dt)

    if not isinstance(tz, int):
        tz = int(tz)
    
    if AM_PM:
        t = datetime.utcfromtimestamp(dt+tz).strftime('%Y-%m-%d %I:%M:%S %p')
    else:
        t = datetime.utcfromtimestamp(dt+tz).strftime('%Y-%m-%d %H:%M:%S')
    
    return t


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
        '&appid=' + OPEN_WEATHER_KEYS.OPEN_WEATHER_API_KEY

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


# ----------------------------------------------------------------------------
"""
    When 'weather-bot.py' is run as a program, this is where the program 
        starts. If another python file is currently the active project, 
        this section is ignored.

    This is where I will test the weather-bot before it is added to the main 
        Hermes Project.
"""
if __name__ == '__main__':
    weather_json = get_weather_json(OPEN_WEATHER_KEYS.lat, OPEN_WEATHER_KEYS.lon)

    if weather_json is not None:
        if 'current' in weather_json:
            print('Current Weather Forecast:')
            # Format available items
            # Format time data
            if 'dt' in weather_json['current']:
                print('\tCurrent Time:\t'+convert_time(weather_json['current']['dt'], weather_json['timezone_offset'], True)[11:])
            if 'sunrise' in weather_json['current']:
                print('\tSunrise:\t'+convert_time(weather_json['current']['sunrise'], weather_json['timezone_offset'], True)[11:])
            if 'sunset' in weather_json['current']:
                print('\tSunset:\t\t'+convert_time(weather_json['current']['sunset'], weather_json['timezone_offset'], True)[11:])
            
            # Add line between time and temp data
            print(' ')

            # Format temperature data
            if 'temp' in weather_json['current']:
                print('\tCurrent Temp:\t'+str(weather_json['current']['temp'])+' F')
            if 'feels_like' in weather_json['current']:
                print('\tFeels Like:\t'+str(weather_json['current']['feels_like'])+' F')
            if 'dew_point' in weather_json['current']:
                print('\tDew Point:\t'+str(weather_json['current']['dew_point'])+' F')
            if 'pressure' in weather_json['current']:
                print('\tPressure:\t'+str(weather_json['current']['pressure'])+' hPa')

            # Add line between temp and sky data
            print(' ')

            # Format Sky Data
            if 'uvi' in weather_json['current']:
                print('\tUV Index:\t'+str(weather_json['current']['uvi'])+' ')
            if 'clouds' in weather_json['current']:
                print('\tCloud Cover:\t'+str(weather_json['current']['clouds'])+' %')
            if 'humidity' in weather_json['current']:
                print('\tHumidity:\t'+str(weather_json['current']['humidity'])+' %')
            if 'visibility' in weather_json['current']:
                print('\tVisibility:\t'+str(weather_json['current']['visibility'])+' meters')

            if 'weather' in weather_json['current']:
                if 'icon' in weather_json['current']['weather'][0]:
                        icon_url = 'http://openweathermap.org/img/wn/' + \
                            weather_json['current']['weather'][0]['icon'] + \
                            '@2x.png'
                        print(icon_url)