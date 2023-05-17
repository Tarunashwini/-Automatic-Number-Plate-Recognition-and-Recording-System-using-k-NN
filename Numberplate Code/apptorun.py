#import streamlit as st
import glob
import Main
import os
import cv2
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk




def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("All Files", "*.*"), ("PNG File", "*.png"),("JPG File", "*.jpg")))
    global txt
    txt = Main.main(fln)
    img = Image.open(fln)
    img = img.resize((500,500))
    img = ImageTk.PhotoImage(img)
    lbl.image = img
    lbl.configure(image=img)

def classify():
    img = Image.open("C:/Users/Tarun/OneDrive/Desktop/Numberplate/SavedImg/R1.png").resize((500,500))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    print("--",txt)
    lbl.configure(text=txt)
    






root = Tk()
root.geometry("500x300")





image_0 = Image.open("C:/Users/Tarun/OneDrive/Desktop/Numberplate/LicPlateImages/wallpaper.webp")
bck_end = ImageTk.PhotoImage(image_0)
lbl = Label(root,image=bck_end)
lbl.place(x=0,y=0)




lbl=Label(root, text="NUMBER PLATE RECOGNITION", font=('Calibri 36'))
lbl.pack(pady=20)


frm = Frame(root,bg="#88cffa")
frm.pack(side=BOTTOM, padx=15, pady = 15)

lbl = Label(root)
lbl.pack()


btn = Button(frm,text = "        Browse        ", command=showimage)
btn.pack(side=tk.LEFT)

btn = Button(frm, text = "        Classify        ", command=classify)
btn.pack(side=tk.RIGHT)



root.title("Image Browsering.... ")

root.mainloop()