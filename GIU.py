import tkinter as tk 
import requests 
from PIL import Image, ImageTk

# dimensions
height = 700
width = 800

# create root window 
root = tk.Tk()

# create a canvas
canvas = tk.Canvas( root, height = height, width = width )
canvas.pack()

# create a frame
frame = tk.Frame(root, bg = '#FE9C9C', bd = 5 )
frame.place( relwidth = 0.75, relheight = 0.1, relx = 0.5, rely = 0.1, anchor = 'n' )

# create an entry bar 
entry = tk.Entry( frame, font = 40 )
entry.place( relwidth = 0.65, relheight = 1 )

# create simple button 
button = tk.Button( frame, text = "test button bitch", font = 40 )
button.place( relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1 )

lowerFrame = tk.Frame( root, bg = '#FE9C9C', bd = 10)
lowerFrame.place( relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n' )

# create a label
label = tk.Label( lowerFrame )
label.place( relwidth = 1, relheight = 1 )

# start GUI loop
root.mainloop()