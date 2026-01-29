import requests

api_key = "test"
city = input("Введите название города: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"Температура: {temp}°C")
    print(f"Погода: {description}")
else:
    print("Ошибка. Проверьте название города или API-ключ.")