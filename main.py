import requests

city = 'Moscow,RU'
appid = '29d09b29d42f90dfe468c166e44d0fd1'
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print(data)