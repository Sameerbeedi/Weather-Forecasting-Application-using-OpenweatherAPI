Weather Forecast Application

This is a simple weather forecast application consisting of a client and server component. The client allows users to enter a city name and fetch the current weather information as well as the forecasted weather for the next 5 days. 
The server fetches the weather data from the OpenWeatherMap API and sends it to the client upon request.
Instructions for Running the Application:

Server:

Run server.py to start the server.
Ensure that you have the necessary SSL certificate and key files (server.crt and server.key) in the specified path. These files are required for establishing a secure connection between the client and the server.
The server listens on its ip address(in code localhost) at port specified(in code 12000).Upon receiving a connection request from a client, the server fetches weather data from the OpenWeatherMap API based on the requested city and 
sends the data back to the client.

Client:

Run client.py to start the client application.
Ensure ip address and port number is same as server's.
Enter the name of the city for which you want to fetch weather information into the input field.
Click the "Fetch weather" button to retrieve the weather data.
The application displays the current weather information, including temperature, description, and a weather icon, as well as the forecasted weather for the next 5 days.

Dependencies:

Python 3.x
tkinter library for GUI components
requests library for making HTTP requests to the OpenWeatherMap API
json library for parsing JSON data
datetime library for working with date and time objects
ssl library for SSL certificate handling
socket library for network communication

Notes:

Ensure that you have an active internet connection to fetch weather data from the OpenWeatherMap API.
You need to replace the placeholder API key (api_key) in server.py with your actual OpenWeatherMap API key.
The SSL certificate and key files provided (server.crt and server.key) are placeholders. Replace them with your actual SSL certificate and key files.
The application currently runs on localhost for testing purposes. Modify the server address (localhost) and port (12000) as necessary for deployment in a production environment.
This application provides a basic user interface for fetching weather information. Additional features and enhancements can be implemented based on specific requirements.



