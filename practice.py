import requests
API="" #add your own api code
x=input("enter the city where you wanna see the weather report: ")
url= "api.openweathermap.org/data/2.5/weather?q="+x+"&APPID="+API
output=requests.get(url)
data=output.json()
weather=data['main']
print("the temperature in your city will be "+weather['temp']+" but it feels like "+weather['feels_like'])
