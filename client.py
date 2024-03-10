import tkinter as tk
from tkinter import *
from tkinter import ttk
import socket
import json
import requests
from datetime import datetime
import ssl

# Import the SSL context from the server code
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"C:\code\cn\server.crt", keyfile=r"C:\code\cn\server.key") # Replace the path with the actual location of your server's SSL context file

def fetch_weather_data(city):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        icon_label_current = tk.Label(second_frame, image=icon_image_current, bg="white")
        icon_label_current.grid(row=1, column=0)
        icon_label_current.image = icon_image_current
    # Display current weather information
    current_weather_label.config(text=f"Current Weather: {current_date}: {current_weather['weather'][0]['description'].capitalize()}  Temp: {current_weather['main']['temp_min']} °C/{current_weather['main']['temp_max']} Wind Speed: {current_weather['wind']['speed']} km/h  Humidity: {current_weather['main']['humidity']}  g/m3")
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
                icon_label = tk.Label(second_frame, image=icon_image, bg="white")
                icon_label.grid(row=r, column=c)
                icon_label.image = icon_image
            label_text = f"{date}: {entry['weather'][0]['description'].capitalize()}  Temp: {entry['main']['temp_min']} °C/{entry['main']['temp_max']} °C    Wind Speed:{entry['wind']['speed']} km/h  Humidity: {entry['main']['humidity']}  g/m3  Time: {entry['dt_txt'][11:]}"
            label = tk.Label(second_frame, text=label_text, bg="white", fg="black")
            label.grid(row=r, column=c+1)
            r += 1

root = tk.Tk()
root.title("Weather Information")
root.configure(bg="white")
root.geometry("760x800")

#for scrollbar
main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)

my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame=Frame(my_canvas)
second_frame.configure(bg="white")
my_canvas.create_window((0,0),window=second_frame,anchor="nw")

#for displaying the text box, and all other labels
city_label = tk.Label(second_frame, text="Enter city:", bg="white", fg="black")
city_label.grid(row=0, column=0)

city_entry = tk.Entry(second_frame)
city_entry.grid(row=0, column=1, padx=5)

submit_button = tk.Button(second_frame, text="Fetch Weather", command=display_weather_info, bg="black", fg="white")
submit_button.grid(row=0, column=2)

current_weather_label = tk.Label(second_frame, text="", bg="white", fg="black")
current_weather_label.grid(row=1, column=0, columnspan=3)

forecast_weather_label = tk.Label(second_frame, text="", bg="white", fg="black")
forecast_weather_label.grid(row=2, column=0, columnspan=3)



root.mainloop()
