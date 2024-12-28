from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from io import BytesIO  # Import BytesIO to handle binary image data
from PIL import Image, ImageTk


# Setting up the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# API Key
API_KEY = "be1116df59e8c95fdb01da17ff24627c"



# Weather Icon Placeholder
weather_icon = Label(root)
weather_icon.place(x=380, y=260)  


# Function to fetch weather details
def get_weather():
    city = textfield.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return
    
    try:
        # Geolocate city
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city, timeout=10)
        if not location:
            messagebox.showerror("Error", "City not found!")
            return

        # Find timezone
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        if not result:
            messagebox.showerror("Error", "Timezone not found for the given location!")
            return

        # Get current local time
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        # Update clock and name labels
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Fetch weather data from OpenWeatherMap API
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(api)
        json_data = response.json()
        
        if json_data.get("cod") != 200:
            messagebox.showerror("Error", json_data.get("message", "Unknown error occurred"))
            return

       # Extracting data
        condition = json_data["weather"][0]["description"]
        temp = json_data["main"]["temp"]
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        
        # Weather icon
        icon_code = json_data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url, stream=True)
        if icon_response.status_code == 200:
            icon_data = BytesIO(icon_response.content)  # Wrap binary content in BytesIO
            icon_image = Image.open(icon_data)  # Open image using PIL
            icon_photo = ImageTk.PhotoImage(icon_image)  # Convert to Tkinter-compatible format
            weather_icon.config(image=icon_photo)
            weather_icon.image = icon_photo  # Save a reference to prevent garbage collection
        
        # Extract sunrise and sunset times (UNIX timestamps)
        sunrise_timestamp = json_data["sys"]["sunrise"]
        sunset_timestamp = json_data["sys"]["sunset"]

        # Convert UNIX timestamp to local time
        sunrise_time = convert_unix_to_local_time(sunrise_timestamp, result)
        sunset_time = convert_unix_to_local_time(sunset_timestamp, result)
        
        
        
        # Update the labels
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition.title()}")
        w.config(text=f"{wind} km/h")
        h.config(text=f"{humidity}%")
        d.config(text=f"{condition}")
        p.config(text=f"{pressure} hPa")
        sunrise_label.config(text=f"Sunrise: {sunrise_time}")
        sunset_label.config(text=f"Sunset: {sunset_time}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        
# Function to convert UNIX timestamp to local time
def convert_unix_to_local_time(unix_timestamp, timezone):
    utc_time = datetime.utcfromtimestamp(unix_timestamp)
    local_time = pytz.timezone(timezone).localize(utc_time)
    return local_time.strftime("%I:%M %p")


# Search Box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(
    root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white"
)
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=get_weather)
myimage_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box
frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(side="bottom", pady=5,padx=5)

# Clock and Name Labels
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20, "bold"))
clock.place(x=30, y=130)


# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Display fields
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="N/A", font=("arial", 15, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="N/A", font=("arial", 15, "bold"), bg="#1ab5ef")
h.place(x=250, y=430)

d = Label(text="N/A", font=("arial", 15, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)

p = Label(text="N/A", font=("arial", 15, "bold"), bg="#1ab5ef")
p.place(x=650, y=430)

# New labels for Sunrise and Sunset
sunrise_label = Label(root, text="Sunrise: N/A", font=("Helvetica", 15, 'bold'))
sunrise_label.place(x=500, y=30)

sunset_label = Label(root, text="Sunset: N/A", font=("Helvetica", 15, 'bold'))
sunset_label.place(x=500, y=60)


root.mainloop()