import ssl
import requests
import socket

import json
from datetime import datetime, timedelta

# Generate SSL certificate
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"D:\college\sem4\CN\mini_project\server.crt", keyfile=r"D:\college\sem4\CN\mini_project\server.key")



# Create a TCP socket object using the imported alias
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 12000))
s.listen(3)
print('Waiting for connections')

def fetch_weather(api_key, city):
    current_date = datetime.now().date()
    end_date = current_date + timedelta(days=5)

    # Format the dates in the required format for the API call
    start_date_str = current_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    url1 = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&start={start_date_str}&end={end_date_str}"
    url2 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print("Start date:", start_date_str)
    print("End date:", end_date_str)
    response1 = requests.get(url1)  # next 5 days weather data
    response2 = requests.get(url2)  # current weather data
    if response1.status_code == 200:
        data1 = response1.json()  # next
        data2 = response2.json()  # current
    else:
        print(f"Failed to fetch weather data for {city}. Status code: {response1.status_code}")
        return

    data1['list'].append(data2)
    json_data = json.dumps(data1)
    c.send(json_data.encode())
    c.close()

while True:
    c, addr = s.accept()
    api_key = 'c708d4e83c861124a8f6c3cb40450dfd'  
    print('Server Started')
    print("Connected with ", addr)
    city = c.recv((1024)).decode()
    print('Received city:', city)
    fetch_weather(api_key, city)