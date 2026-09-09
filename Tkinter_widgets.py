# 1. The Pillow (PIL) Library

# Pillow is a Python library used to open, edit,
# resize and save images.
#
# Install it using:
# pip install pillow

from PIL import Image

image = Image.open("photo.jpg")

print(image.size)


# 2. Adding Images in Tkinter

# PhotoImage is used to display images in Tkinter.
# Pillow can be used for formats such as JPG and PNG.

from tkinter import *
from PIL import Image, ImageTk

window = Tk()

image = Image.open("photo.jpg")
image = image.resize((200, 150))

photo = ImageTk.PhotoImage(image)

label = Label(window, image=photo)
label.pack()

window.mainloop()


# 3. Messagebox Widget

# messagebox is used to display popup messages
# to the user.

from tkinter import *
from tkinter import messagebox

window = Tk()

messagebox.showinfo("Welcome", "Hello, welcome!")

window.mainloop()


# 4. Messagebox Function Types

# Common messagebox functions:
#
# showinfo()    -> Information message
# showwarning() -> Warning message
# showerror()   -> Error message
# askyesno()    -> Asks Yes or No

from tkinter import *
from tkinter import messagebox

window = Tk()

messagebox.showinfo("Info", "Task completed.")
messagebox.showwarning("Warning", "Low battery.")
messagebox.showerror("Error", "Something went wrong.")

answer = messagebox.askyesno("Question", "Do you want to continue?")

print(answer)

window.mainloop()


# 5. Toplevel Window

# Toplevel() creates a new window in addition
# to the main Tkinter window.

from tkinter import *

window = Tk()

window.title("Main Window")

def open_window():
    new_window = Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("300x200")

    Label(new_window, text="This is a Toplevel Window").pack()

Button(window, text="Open New Window", command=open_window).pack()

window.mainloop()