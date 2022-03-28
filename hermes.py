# Import Hermes submodules
import weatherbot
import emailmanager
import EMAIL_KEYS

# ----------------------------------------------------------------------------
"""
    Use the WeatherManager module to generate a text-only summary of the current weather forecast.
    
    Inputs:
        data -> JSON
            JSON data-set containing current weather data

    Output:
        Single string containing text-only summary for email bot to send
"""
def generate_email_text(data):
    email_text = ''

    if data is not None:
        email_text += 'Today\'s Weather Forecast for West Lafayette, IN\n\n'

        if 'current' in data:
            email_text += 'It is currently:\n'

            # Format available items
            # Format time data
            if 'dt' in data['current']:
                email_text += '\tTime:\t'+weatherbot.convert_time(data['current']['dt'], data['timezone_offset'], True)[11:]+'\n'
            
            email_text += '\n'

            # Add temperature data
            if 'temp' in data['current']:
                email_text += '\tTemperature:\t'+str(data['current']['temp'])+' °F'+'\n'
            if 'feels_like' in data['current']:
                email_text += '\tFeels Like:\t'+str(data['current']['feels_like'])+' °F'+'\n'
            if 'dew_point' in data['current']:
                email_text += '\tDew Point:\t'+str(data['current']['dew_point'])+' °F'+'\n'
            if 'pressure' in data['current']:
                email_text += '\tPressure:\t'+str(data['current']['pressure'])+' hPa'+'\n'

            email_text += '\n'

            # Add Sky Data
            if 'uvi' in data['current']:
                email_text += '\tUV Index:\t'+str(data['current']['uvi'])+' '+'\n'
            if 'clouds' in data['current']:
                email_text += '\tCloud Cover:\t'+str(data['current']['clouds'])+' %'+'\n'
            if 'humidity' in data['current']:
                email_text += '\tHumidity:\t'+str(data['current']['humidity'])+' %'+'\n'
            if 'visibility' in data['current']:
                email_text += '\tVisibility:\t'+str(data['current']['visibility'])+' meters'+'\n'

        if 'daily' in data:
            email_text += '\nFor the rest of today:\n'

            if 'sunrise' in data['daily'][0]:
                email_text += '\tSunrise:\t'+weatherbot.convert_time(data['daily'][0]['sunrise'], data['timezone_offset'], True)[11:]+'\n'
            if 'sunset' in data['daily'][0]:
                email_text += '\tSunset:\t\t'+weatherbot.convert_time(data['daily'][0]['sunset'], data['timezone_offset'], True)[11:]+'\n'

            if 'moonrise' in data['daily'][0]:
                email_text += '\tMoonrise:\t'+weatherbot.convert_time(data['daily'][0]['moonrise'], data['timezone_offset'], True)[11:]+'\n'
            if 'moonset' in data['daily'][0]:
                email_text += '\tMoonset:\t'+weatherbot.convert_time(data['daily'][0]['moonset'], data['timezone_offset'], True)[11:]+'\n'
            
            email_text += '\n'

            if 'temp' in data['daily'][0]:
                if 'min' in data['daily'][0]['temp']:
                    email_text += '\tMin Temp.:\t'+str(data['daily'][0]['temp']['min'])+' °F\n'
                if 'max' in data['daily'][0]['temp']:
                    email_text += '\tMax Temp.:\t'+str(data['daily'][0]['temp']['max'])+' °F\n'
            
            if 'weather' in data['daily'][0]:
                if 'description' in data['daily'][0]['weather']:
                    email_text += '\t'+str(data['daily'][0]['weather']['description']).capitalize()+'\n'

            if 'alerts' in data['daily'][0]:
                email_text += '\n\nWeather Alerts for Today:\n\n'

                for a in data['daily'][0]['alerts']:
                    email_text += str(a['event'])+'\n'
                    email_text += '----------------------------------------\n'
                    email_text += str(a['description']) + '\n\n'

    
    return email_text


if __name__ == '__main__':

    email_text = generate_email_text(weatherbot.get_weather_json())
    subject = "Today's Weather Forecast."

    emailmanager.send_text_email(email_text, subject, EMAIL_KEYS.RECIPIENTS)