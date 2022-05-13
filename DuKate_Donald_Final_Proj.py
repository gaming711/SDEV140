from tkinter import *


def calc1():
    Savings = float(yearlyCont.get())
    NumYR = float(numyears.get())
    MonCont = float(monthCont.get())
    SAV: float = Savings * (pow((1.10 / 1), (1 * NumYR)))
    print(SAV)

    half: float = (pow((1.10), (NumYR)) - 1) / .10
    print(half)
    future: float = MonCont * half
    print(future)
    total: float = SAV + future

    display_total_amt_label["text"] = str(total)

    # Total_amt = weeklyCont*(pow(((1.10/12)), 12*5))
    # display_total_amt_label["text"] = (Total_amt)


def calc2():
    Savings = float(yearlyCont.get())
    NumYR = float(numyears.get())
    MonCont = float(monthCont.get())
    SAV: float = Savings * (pow((1.12 / 1), (1 * NumYR)))

    half: float = (pow((1.12), (NumYR)) - 1) / .12
    future: float = MonCont * half
    total: float = SAV + future

    display_total_amt_label2["text"] = str(total)


def calc3():
    Savings = float(yearlyCont.get())
    NumYR = float(numyears.get())
    MonCont = float(monthCont.get())
    SAV: float = Savings * (pow((1.15 / 1), (1 * NumYR)))

    half: float = (pow((1.15), (NumYR)) - 1) / .15
    future: float = MonCont * half
    total: float = SAV + future

    display_total_amt_label3["text"] = str(total)


mainWindow = Tk()

# frame1
frame1 = LabelFrame(mainWindow, text="Frame 1", padx=30, pady=30)
frame1.grid(row=0, column=0, columnspan=10, rowspan=10)
# frame2
frame2 = LabelFrame(mainWindow, text="Frame 2", padx=30, pady=30)
frame2.grid(row=0, column=25, columnspan=10, rowspan=10)

# add items to frame1
yearlyCont = Label(frame1, text="Enter beginning principal")
yearlyCont.grid(row=2, column=0)

numyears = Label(frame1, text="Enter number of years")
numyears.grid(row=4, column=0)

monthCont = Label(frame1, text="Enter monthly contribution")
monthCont.grid(row=6, column=0)

display_total_amt_label = Label(frame2)
display_total_amt_label.grid(row=0, column=40)

display_total_amt_label2 = Label(frame2)
display_total_amt_label2.grid(row=2, column=40)

display_total_amt_label3 = Label(frame2)
display_total_amt_label3.grid(row=4, column=40)

yearlyCont = Entry(frame1, width=20)
yearlyCont.grid(row=2, column=5)

numyears = Entry(frame1, width=20)
numyears.grid(row=4, column=5)

monthCont = Entry(frame1, width=20)
monthCont.grid(row=6, column=5)

calcButton = Button(frame2, text="Calculate 10% return", bg="white", fg="red", command=calc1)
calcButton.grid(row=0, column=30)

calcButton2 = Button(frame2, text="Calculate 12% return", bg="white", fg="red", command=calc2)
calcButton2.grid(row=2, column=30)

calcButton3 = Button(frame2, text="Calculate 15% return", bg="white", fg="red", command=calc3)
calcButton3.grid(row=4, column=30)

mainWindow.mainloop()