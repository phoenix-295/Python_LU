from tkinter import Tk, Entry, Button, Label

master = Tk()


def fun1():
    data1 = ol.get()
    print("Hello ", data1)


button = Button(master, text="Click me", width=25, command=fun1)
ol = Entry(master)
label1 = Label(master, text="Start counter")


button.grid(row=0, column=0)
ol.grid(row=0, column=1)
label1.grid(row=1, column=0)


master.mainloop()
