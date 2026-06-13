'''Photos Slideshow Album Application'''

import tkinter as tk
import time
from PIL import Image, ImageTk

#Main Window
root=tk.Tk()
root.title("Photos Slideshow Album")
root.geometry("900x900")

#List of image paths
image_paths = [
    r'C:/Users/USER/OneDrive/Desktop/pic/21.jpg',
    r'C:/Users/USER/OneDrive/Desktop/pic/IMG_20140526_144801.jpg',
    r'C:/Users/USER/OneDrive/Desktop/pic/IMG_20140524_164345.jpg',
    r'C:/Users/USER/OneDrive/Desktop/pic/2013-04-04 07.28.04.jpg',
    r'C:/Users/USER/OneDrive/Desktop/pic/2012-08-19 10.22.53.jpg'
]

#Convert image paths to PIL images and resize them
image_size=(700,700)
images=[]
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)

#Convert PIL images to Tkinter compatible images
tk_images=[]
for img in images:
    tk_img=ImageTk.PhotoImage(img)
    tk_images.append(tk_img)

#Label to display images
image_label=tk.Label(root)
image_label.pack(pady=30)   

#Slideshow function
def start_slideshow():
    for photo in tk_images:
        image_label.config(image=photo)
        image_label.image=photo # Keep a reference to avoid garbage collection
        root.update()
        time.sleep(2) # Display each image for 2 seconds

#Button to start slideshow
play_button=tk.Button(
    root,
    text="Play Slideshow",
    font=("Arial",20),
    command=start_slideshow
)

play_button.pack(pady=40) # packing the button 


root.mainloop() #Start the main event loop to run the application
