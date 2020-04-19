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
frame = tk.Frame(root, bg = '#80c1ff' )
frame.place( relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1 )

# create simple button 
button = tk.Button( frame, text = "test button bitch", bg = 'gray' )
# button.pack( side = 'left', fill = 'both', expand = True )
# button.grid( row = 0, column = 0 )
button.place( relx = 0, rely = 0, relwidth = 0.25, relheight = 0.25 )

# create a label
label = tk.Label( frame, text = "label, bitch", bg = "yellow" )
# label.pack( side = 'left', fill = 'both' )
# label.grid( row = 0, column = 1 )
label.place( relx = 0.3, rely = 0, relwidth = 0.45, relheight = 0.25 )

# create an entry bar 
entry = tk.Entry( frame, bg = 'green' )
# entry.pack( side = 'left', fill = 'both' )
# entry.grid( row = 0, column = 2 )
entry.place( relx = 0.8, rely = 0, relwidth = 0.2, relheight = 0.25 )

# start GUI loop
root.mainloop()