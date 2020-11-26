from tkinter import Button, Tk, Entry, Label, Toplevel

master = Tk()
a = 600


def OpenWindow():
    newWindow = Toplevel(master)
    newWindow.title("Counter")
    newWindow.geometry("400x400")
    mes = "Keep Calm\n & \n Learn Python"
    Label(newWindow, text=mes, bg='red').pack()


def fun2():
    global a
    a = a-1
    if a <= -1:
        OpenWindow()
        return None
    label2.configure(text=a, font=('Helvetica', 16))
    master.after(1000, fun2)


def fun1():
    try:
        e_data = e1.get()
        global a
        a = int(e_data)
    except Exception as e:
        print(e)
    fun2()


label1 = Label(master, text="Fill Seconds", font=('Helvetica', 16), width=15)
label2 = Label(master, text="0", font=('Helvetica', 16))
e1 = Entry(master)
# b1 = Button(master, text="Start", width=25, command=fun1, bg=background color ,fg=foreground color)
b1 = Button(master, text="Start", width=25,
            command=fun1, font=('Helvetica', 16))

label1.grid(row=0, column=0)
e1.grid(row=0, column=1)
label2.grid(row=1, column=0)
b1.grid(row=2, column=0)

master.mainloop()
