from tkinter import *
import time
import datetime
import winsound


def alarm_clock(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg = "Current Time: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
            break


def alarm_time():
    alarm_set_time = f"{hour.get()}:{mint.get()}:{sec.get()}"
    alarm_clock(alarm_set_time)


# GUI
alarm = Tk()
alarm.title("Alarm Clock")
alarm.config(width=400, height=180, bg="#FF2400")

clock = Label(text="Set Time in 24 Hour Format!",fg="white",bg="#FF2400",font=20)
clock.place(x=90,y=140)

time_format = Label(text="Set Your Alarm:",fg="white",bg="#FF2400",font=("Courier",16,"bold"))
time_format.place(x=0, y=40)

hour_label = Label(text="Hour",fg="white",bg="black",font=18)
hour_label.place(x=200)

mint_label = Label(text="Min",fg="white",bg="black",font=18)
mint_label.place(x=255)

sec_label = Label(text="Sec",fg="white",bg="black",font=18)
sec_label.place(x=305)

hour = StringVar()
mint = StringVar()
sec = StringVar()

hour = Entry(textvariable=hour, bg="#ADD8E6", width=4, font=(20,))
hour.place(x=200,y=40)

mint = Entry(textvariable=mint, bg="#ADD8E6", width=4, font=(20,))
mint.place(x=250, y=40)

sec = Entry(textvariable=sec, bg="#ADD8E6", width=4, font=(20,))
sec.place(x=300, y=40)

submit = Button(text="Set Your Alarm", fg="black", bg="Yellow",width=16, command=alarm_time,font=24)
submit.place(x=120,y=90)


alarm.mainloop()