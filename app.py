import requests

api_key = '259e89dd8342eb952c5d76c79aae5154'

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No city found") 

else:
    weather = weather_data.json()['weather'][0]['main']
    #here you get the temperature in F
    temp = round(weather_data.json()['main']['temp'])
    
    #convert to F to C
    temp = 5 / 9 * (temp - 32)

    print("Weather in %s: %s" % (user_input, weather))
    print("Temperature in %s is %d °C" % (user_input, temp))

