Weather Forecasting Application
1. server.py
This script handles the server-side logic, including:

Setting up a secure connection using SSL.
Listening for client requests on a specified port.
Fetching weather data from the OpenWeatherAPI based on the city name received from the client.
Sending current weather data and a 5-day forecast back to the client.
2. client.py
This script manages the client-side user interface and communication, including:

Creating a GUI using Tkinter for user interaction.
Sending the city name to the server when requested by the user.
Receiving and displaying current weather data and the 5-day forecast from the server.
Extracting morning and evening weather data for the next 5 days.

Dependencies
Ensure that the following Python libraries are installed:

tkinter: For GUI components.
requests: For making HTTP requests to the OpenWeatherAPI.
json: For parsing the JSON data received from the API request.
datetime: For handling date and time in the weather data.
ssl: For SSL certificate handling.
socket: For network communication.
How to Run the Project
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Sameerbeedi/Weather-Forecasting-Application-using-OpenweatherAPI/tree/main.git
Navigate to the project directory:

bash
Copy code
cd Weather-Forecasting-App
Run the server:

bash
Copy code
python server.py
Ensure that the necessary SSL files are present on the server machine and the correct paths are set in the program.
Make sure the server is listening on the desired port (default: 12000) and has an active internet connection.
Run the client:

bash
Copy code
python client.py
In the fetch_weather function, replace 'localhost' with the server's IP address.
Enter the city name for which you want to fetch weather data and click "Fetch Weather."
Note
Replace the API key in server.py with an active OpenWeatherAPI key.
Ensure that the port number in the client matches the server's port number.
Replace the SSL filenames with the actual file names and provide the correct paths.
