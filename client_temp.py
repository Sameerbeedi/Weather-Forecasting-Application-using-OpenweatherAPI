import socket as tcp_socket
import socket
import ssl
import json
import requests
from datetime import datetime
import tkinter as tk
from tkinter import ttk


# Import the SSL context from the server code
# Replace the path with the actual location of your server's SSL context file
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"D:\college\sem4\CN\mini_project\server.crt", keyfile=r"D:\college\sem4\CN\mini_project\server.key")

def fetch_weather_data(city):
    c = socket.socket()
    c.connect(('localhost', 12000))
    c.send(bytes(city, 'utf-8'))
    rec_data = c.recv(20480).decode()
    c.close()
    return json.loads(rec_data)

def download_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    response = requests.get(icon_url)
    if response.status_code == 200:
        img_data = response.content
        return tk.PhotoImage(data=img_data)
    else:
        print(f"Failed to download icon for code: {icon_code}")
        return None

def display_weather_info():
    city = city_entry.get()
    weather_data = fetch_weather_data(city)

    # Extract current weather data
    current_weather = weather_data['list'][-1]  # Last item is the current weather
    current_date = datetime.strptime(weather_data['list'][0]['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
    icon_image_current=download_icon(current_weather['weather'][0]['icon'])
    if icon_image_current:
        icon_label_current = tk.Label(root, image=icon_image_current, bg="white")
        icon_label_current.grid(row=1, column=0)
        icon_label_current.image = icon_image_current
    # Display current weather information
    current_weather_label.config(text=f"Current Weather: {current_date}: {current_weather['weather'][0]['description'].capitalize()}  Temp: {current_weather['main']['temp']} °C")
    current_weather_label.grid(row=1,column=1)
    # Extract and display forecasted weather data for the next 5 days
    forecast_weather_label.config(text="Forecasted Weather:")
    r = 2
    c = 0
    for entry in weather_data['list'][:-1]:  # Exclude the last item (current weather)
        timestamp = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        hour=timestamp.hour
        date = timestamp.date()
        if date != current_date and 6<= hour <12 or 18<= hour <24:
            icon_code = entry['weather'][0]['icon']
            icon_image = download_icon(icon_code)
            if icon_image:
                icon_label = tk.Label(root, image=icon_image, bg="white")
                icon_label.grid(row=r, column=c)
                icon_label.image = icon_image
            label_text = f"{date}: {entry['weather'][0]['description'].capitalize()}  Temp: {entry['main']['temp']} °C Time: {entry['dt_txt'][11:]}"
            label = tk.Label(root, text=label_text, bg="white", fg="black")
            label.grid(row=r, column=c+1)
            r += 1

root = tk.Tk()
root.title("Weather Information")
root.configure(bg="white")

city_label = tk.Label(root, text="Enter city:", bg="white", fg="black")
city_label.grid(row=0, column=0)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=5)

submit_button = tk.Button(root, text="Fetch weather", command=display_weather_info, bg="black", fg="white")
submit_button.grid(row=0, column=2)

current_weather_label = tk.Label(root, text="", bg="white", fg="black")
current_weather_label.grid(row=1, column=0, columnspan=3)

forecast_weather_label = tk.Label(root, text="", bg="white", fg="black")
forecast_weather_label.grid(row=2, column=0, columnspan=3)

# scrollbar = ttk.Scrollbar(root,orient='vertical', command=text.yview)
# scrollbar.grid(row=0,column=2,sticky=tk.NS)
# text['yscrollcommand']=scrollbar.set

# scrollbar = ttk.Scrollbar(root, orient='vertical', command=root.yview)
# scrollbar.grid(row=1, column=3, rowspan=2, sticky='ns')
# root.configure(yscrollcommand=scrollbar.set)

root.mainloop()