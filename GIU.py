import tkinter as tk 
import requests 
from PIL import Image, ImageTk

"""
    First time using the Python tkinter module. Simple Weather app.
"""

apiKey = '8628589b3c4436084b467a9911675e0e'
endpoint = 'api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}'

# dimensions
height = 700
width = 800

def get_weather( city ):
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': apiKey, 'q': city, 'units': 'imperial'}
    response = requests.get( endpoint, params = params )
    weather = response.json()
    label['text'] = weatherFormat( weather )

def weatherFormat( weather ):
    try:
        name = weather['name']
        mainWeather = weather['weather'][0]['main']
        temp = weather['main']['temp'] 
        returnString = 'City: ' + str( name ) + '\n' + ' Weather: ' + str( mainWeather ) + '\n' + 'Temperature: ' + str( temp ) 
    except:
        returnString = 'There was a problem retrieving that information'
    return returnString

# create root window and set title
root = tk.Tk()
root.title( 'Weather Widget' )

# create a canvas
canvas = tk.Canvas( root, height = height, width = width )
canvas.pack()

# set background image 
background_image = ImageTk.PhotoImage( Image.open( 'background.jpg' ) )
background_label = tk.Label( root, image = background_image )
background_label.place( relwidth = 1, relheight = 1 )

# create a frame
frame = tk.Frame(root, bg = '#FE9C9C', bd = 5 )
frame.place( relwidth = 0.75, relheight = 0.1, relx = 0.5, rely = 0.1, anchor = 'n' )

# create an entry bar 
entry = tk.Entry( frame, font = 40 )
entry.place( relwidth = 0.65, relheight = 1 )

# create simple button 
button = tk.Button( frame, text = "Get Weather", font = 40, command = lambda: get_weather( entry.get() )  )
button.place( relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1 )

lowerFrame = tk.Frame( root, bg = '#FE9C9C', bd = 10)
lowerFrame.place( relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n' )

# create a label
label = tk.Label( lowerFrame )
label.place( relwidth = 1, relheight = 1 )

# start GUI loop
root.mainloop()