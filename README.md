# WEATHER FORECASTING APPLICATION<br>
This is a client-server application which fetches weather data from the OpenWeatherAPI.<br>
- The client enters a city, and sends the city name to the server, and the server fetches weather data for that city and sends it to the client.
- The server sends the current weather data, and the weather data for the next 5 days.
- The client extracts the data for the morning and evening for the next 5 days, and the current weather data.

## Instructions for running the application:
- Server -Run the server.py program to start the server -Ensure that the necessary SSL files are in the server pc and the correct path is in the program. -The server is now listening for connections on 'localhost' and port 12000. If you want to change the port, make sure that the client is connected to the same port. -Ensure that the server pc has an active internet connection to fetch weather data from the API
- Client -In the fetch_weather function, replace 'localhost' with the IP address of the server. -Run the program. -Enter the city for which you want to fetch weather data. -Click on the "Fetch Weather" button. -The current weather and the weather for the next 5 days is displayed.
## Dependencies:<br>
- Python 3.x -tkinter: for GUI components 
- requests: for making HTTP requests to the OpenWeathermap API 
- json: for parsing the JSON data received from the API request -datetime: for working on the json object and displaying the weather info for a specific date 
- ssl: for SSL certificate handling -socket: for network communication

### Note:<br>
- Ensure that you have an active internet connection.
- Replace 'localhost' with the IP Address of the server in the client and ensure that the port number in the client is the same as the port number in the server.
- Replace the 'server.crt' and the 'server.key' filenames with their actual file names and put the correct path.
- Replace the API Key with an active API key.
