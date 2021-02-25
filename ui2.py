import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk  ####ต้องมี

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width= 50, height=50)
imageFrame.grid(row=0, column=0, padx=0, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
canvas = tk.Canvas(window, width = 300, height = 300)
canvas.pack()
image =Image.open("bibi.jpg")
image = image.resize((300, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
canvas.create_image(20, 20, anchor=NW, image=img)

#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=1000, height= 100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI