from tkinter import *

w = Tk()
w.title("My Profile Card")
w.geometry("400x300")
Label(w, text="My Profile Card", bg="purple", fg="white", width=40).grid(
    row=0, columnspan=2
)
Label(w, text="Name:").grid(row=1, column=0)
n = Entry(w)
n.grid(row=1, column=1)
Label(w, text="Hobby:").grid(row=2, column=0)
h = Entry(w)
h.grid(row=2, column=1)
Label(w, text="About Me:").grid(row=3, columnspan=2)
a = Text(w, width=40, height=4)
a.grid(row=4, columnspan=2)
Button(w, text="Show My Card", bg="purple", fg="white").grid(row=5, columnspan=2)
w.mainloop()
