from tkinter import *
from datetime import datetime
import winsound
import time

def alarm(a,b,c):
    while True:
        time.sleep(1)
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")
        if a == current_period:
            if b == current_hour:
                if c == current_min:
                    winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                    break
def setalm():
    times_alarm=Tk()
    times_alarm.attributes('-topmost',True)
    times_alarm.geometry("900x700")
    times_alarm["bg"]="#D9D8D7"
    hour2=Label(times_alarm,text="Hour(hh)",bg='white',fg='purple',font=('Cambria',18))
    hour2.place(x=200,y=300)
    sethour=Entry(times_alarm,width=15,bg='white',fg='green',font=('Cambria',18))
    sethour.place(x=200,y=380)
        
    minuts=Label(times_alarm,text="Minutes(mm)",bg='white',fg='purple',font=('Cambria',18))
    minuts.place(x=400,y=300)
    setminuts=Entry(times_alarm,width=15,bg='white',fg='green',font=('Cambria',18))
    setminuts.place(x=400,y=380)
        
    alarm_per=Label(times_alarm,text="AM/PM",bg='white',fg='purple',font=('Cambria',18))
    alarm_per.place(x=600,y=300)
    setalarm_per=Entry(times_alarm,width=15,bg='white',fg='green',font=('Cambria',18))
    setalarm_per.place(x=600,y=380)
    def argument():
        a=setalarm_per.get()
        b=sethour.get()
        c=setminuts.get()
        alarm(a,b,c)
    Button(times_alarm,text="Set",bg='white',fg='blue',font=('Cambria',18),command=argument).place(x=700,y=470)
    
setalm()
