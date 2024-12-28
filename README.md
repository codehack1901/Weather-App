# Weather App

## Overview

Weather App is a Python-based graphical user interface (GUI) application that allows users to get real-time weather information for a specified city. It displays various weather details such as temperature, wind speed, humidity, pressure, and weather description. Additionally, it shows sunrise and sunset times, adjusting the local time based on the city's timezone.

## Features

- **Real-time Weather Data**: Fetches current weather information including temperature, wind speed, humidity, and pressure.
- **Weather Icon**: Displays the weather condition using an icon retrieved from OpenWeatherMap.
- **Timezone-based Local Time**: Displays the current local time for the city.
- **Sunrise and Sunset**: Displays the local sunrise and sunset times.
- **User-friendly GUI**: Built using `Tkinter`, with an easy-to-use interface for city input and weather display.

## Technologies Used

- **Python**: The programming language used to build the app.
- **Tkinter**: Python’s standard GUI toolkit for building the user interface.
- **Geopy**: To convert city names to geographical coordinates (latitude and longitude).
- **TimezoneFinder**: To find the timezone for the given city based on its geographical coordinates.
- **Requests**: To fetch data from OpenWeatherMap API.
- **Pillow**: To handle and display weather icons.
- **pytz**: To handle timezone-related functionality.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python's package installer)

### Steps

1. Clone the repository to your local machine:
   ```bash
    git clone https://github.com/yourusername/Weather-App.git
   ```
2. Navigate to the project directory:

   ```bash
    cd Weather-App
   ```
3. Install the required Python packages:

   ```bash
    pip install -r requirements.txt
   ```
4. Create a file named .env or replace the API_KEY in the code with your own API key obtained from OpenWeatherMap.

5. Run the app:
   ```bash
    python weather_app.py
   ```
   
## Usage

1. **Launch the App**: After running the app, the graphical interface will appear.
   
2. **Enter a City Name**: In the text field at the top of the window, type the name of the city for which you want to check the weather. Click the search icon (magnifying glass) to fetch 
  the data.
  
3. **View the Results**: The weather data will be displayed on the GUI, including:
   - Temperature in Celsius
   - Weather condition (e.g., clear sky, rainy)
   - Wind speed
   - Humidity
   - Pressure
   - Sunrise and sunset times
 
4. **Clock and Time Zone**: The local time of the city will also be shown based on the retrieved timezone.

## API Integration

This app uses the OpenWeatherMap API to fetch weather data. To get an API key:
  1. Go to OpenWeatherMap.
  2. Sign up and get an API key.
  3. Replace the API_KEY variable in the code with your key.

## Screenshot

![Weather App Screenshot](initialscreen.png,finalscreen.png)

   
