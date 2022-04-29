import time
from tkinter import *

from playsound import playsound

root = Tk()
root.title("My Timer")
root.geometry("400x600")
root.config(bg='#000')
root.resizable(False, False)

heading = Label(root, text="Timer", font="arial 30 bold", bg='#000', fg="#ea3548")
heading.pack(pady=10)

Label(root, text="current time", font="arial 15 bold", bg="papaya whip").place(x=65, y=70)


def clock():
    clock_time = time.strftime("%I:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font="arial 15 bold", text="", bg="#fff", fg="#000")

current_time.place(x=190, y=70)
clock()

hours = StringVar()
Entry(root, textvariable=hours, width=2, font="arial 60", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hours.set("00")

minutes = StringVar()
Entry(root, textvariable=minutes, width=2, font="arial 60", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
minutes.set("00")

seconds = StringVar()
Entry(root, textvariable=seconds, width=2, font="arial 60", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
seconds.set("00")

down = 230
left = 50
Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=113 - left, y=down)

Label(root, text="minutes", font="arial 12", bg="#000", fg="#fff").place(x=213 - left, y=down)

Label(root, text="seconds", font="arial 12", bg="#000", fg="#fff").place(x=333 - left, y=down)


def brush():
    hours.set("00")
    minutes.set("02")
    seconds.set("00")


def face():
    hours.set("00")
    minutes.set("15")
    seconds.set("00")


def eggs():
    hours.set("00")
    minutes.set("10")
    seconds.set("00")


def Timer():
    times = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    while times > -1:
        minu, sec = divmod(times, 60)
        hr = 0
        if minu > 60:
            hr, minu = divmod(minu, 60)

        seconds.set(sec)
        minutes.set(minu)
        hours.set(hr)

        root.update()
        time.sleep(1)

        if times == 0:
            playsound("files/alarm.wav")
            seconds.set("00")
            minutes.set("00")
            hours.set("00")

        times -= 1


button = Button(root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold",
                command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)


image1 = PhotoImage(file="files/brush.png")
button1 = Button(root, image=image1, bg="#000", bd=0, command=brush)
button1.place(x=7, y=300)

image2 = PhotoImage(file="files/face.png")
button2 = Button(root, image=image2, bg="#000", bd=0, command=face)
button2.place(x=137, y=300)

image3 = PhotoImage(file="files/eggs.png")
button3 = Button(root, image=image3, bg="#000", bd=0, command=eggs)
button3.place(x=267, y=300)

mainloop()
