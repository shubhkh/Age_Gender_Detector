# importing necessary Labraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy 
import numpy as np

from tensorflow.keras.models import load_model


# Loading the model
from keras.models import load_model
model=load_model("Age_Sex_Detection.keras")


# Intializing the GUI

top=tk.Tk()
top.gemoetry("800x600")
top.title("Age & Gender Detector")
top.configure(background="#CDCDCD")

# Intializing the labels(1 for age and 1 for sex)
label1 = Label(top,background="#CDCDCD",font=("arial",15,"bold"))
label2 = Label(top,background="#CDCDCD",font=("arial",15,"bold"))
sign_image=Label(top)

label1.pack(side="bottom",pady=50)
label2.pack(side="bottom",pady=50)
heading=Label(top,text="Age and Gender  Detector",pady=20,font=("arial",20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()

