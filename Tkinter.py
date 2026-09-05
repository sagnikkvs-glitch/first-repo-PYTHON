# 1. What is Tkinter?

# Tkinter is Python's built-in library used to create
# Graphical User Interface (GUI) applications.
#
# GUI applications contain windows, buttons, labels,
# text boxes, etc.


# 2. Creating a Tkinter Window

# Tk() creates the main window.
# mainloop() keeps the window running.

from tkinter import *

window = Tk()

window.title("My First Window")
window.geometry("300x200")

window.mainloop()


# 3. Label and Button Widgets

# Label is used to display text.
# Button is used to perform an action when clicked.

from tkinter import *

window = Tk()

label = Label(window, text="Hello Tkinter")
label.pack()

button = Button(window, text="Click Me")
button.pack()

window.mainloop()


# 4. Entry, Text, and Frame Widgets

# Entry -> Single-line input
# Text -> Multi-line input
# Frame -> Container for organizing widgets

from tkinter import *

window = Tk()

frame = Frame(window)
frame.pack()

entry = Entry(frame)
entry.pack()

text = Text(frame, height=4, width=20)
text.pack()

window.mainloop()


# 5. Tkinter Grid

# grid() arranges widgets in rows and columns.

from tkinter import *

window = Tk()

label1 = Label(window, text="Name:")
label1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

button = Button(window, text="Submit")
button.grid(row=1, column=1)

window.mainloop()


# Tk()         -> Creates a window
# mainloop()   -> Keeps the window open
# Label()      -> Displays text
# Button()     -> Creates a button
# Entry()      -> Single-line input
# Text()       -> Multi-line input
# Frame()      -> Groups widgets
# grid()       -> Arranges widgets in rows and columns
# pack()       -> Simple widget placement