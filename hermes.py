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
        if 'current' in data:
            email_text += 'Current Weather Forecast:\n\n'

            # Format available items
            # Format time data
            if 'dt' in data['current']:
                email_text += '\tCurrent Time:\t'+weatherbot.convert_time(data['current']['dt'], data['timezone_offset'], True)[11:]+'\n'
            if 'sunrise' in data['current']:
                email_text += '\tSunrise:\t'+weatherbot.convert_time(data['current']['sunrise'], data['timezone_offset'], True)[11:]+'\n'
            if 'sunset' in data['current']:
                email_text += '\tSunset:\t\t'+weatherbot.convert_time(data['current']['sunset'], data['timezone_offset'], True)[11:]+'\n'
            
            email_text += '\n'

            # Add temperature data
            if 'temp' in data['current']:
                email_text += '\tCurrent Temp:\t'+str(data['current']['temp'])+' F'+'\n'
            if 'feels_like' in data['current']:
                email_text += '\tFeels Like:\t'+str(data['current']['feels_like'])+' F'+'\n'
            if 'dew_point' in data['current']:
                email_text += '\tDew Point:\t'+str(data['current']['dew_point'])+' F'+'\n'
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
    
    return email_text


if __name__ == '__main__':

    email_text = generate_email_text(weatherbot.get_weather_json())
    subject = "Today's Weather Forecast."

    emailmanager.send_text_email(email_text, subject, EMAIL_KEYS.RECIPIENTS)