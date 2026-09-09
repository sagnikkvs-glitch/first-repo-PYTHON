import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.title("my photo album")
window.geometry("400x420")

title = Label(window, text= "my photo album" , fg="white",  bg="purple" , width = 40)
title.pack(pady=10)
img_file = Image.open("Screenshot 2026-03-13 172116.png")
img_file= img_file.resize((300, 180))
photo = imageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=10)

def show_message():
    messagebox.showinfo("great", "yoou clicjkd the photo")

msg_btn = Button(
    window, text="click to react", bg ="blue", fg="white", command=show_message
)
msg_btn.pack(pady=5)

def show_details():
    top = Toplevel()
    top.title("photo details")
    top.geometry("300x200")
    info= Label(top, text="taken on : 1 june  2025")
    info.pack(pady= 10)
    placew = Label(top, text="location: my garden")
    placew.pack()
    top.mainloop()