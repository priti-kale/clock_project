from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*
import datetime
from playsound import playsound
root=Tk()
root.geometry("600x200")
def alarm():
    if x.get()=="AM":
        h=int(c.get())
        m=int(c1.get())
    if x.get()=="PM":
        h=int(c.get())
        m=int(c1.get())
    showinfo("alarm notication","alarm has been set")
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
                playsound("https://musikringtone.com//downloads//3394//")
                showinfo("alarm notificarion","wake upke")
root.title(" my alaram clock")
l1=Label(root,text="set alarm hour")
l1.grid(row=0,column=0)
hour=list(range(0,13))
c=Combobox(root,values=hour)
c.grid(row=0,column=1)
 
l2=Label(root,text="set alarm minute")
l2.grid(row=1,column=0)
minute=list(range(1,61))
c1=Combobox(root,values=minute)
c1.grid(row=1,column=1 )

x=Combobox(root,value=["AM","PM"])
x.grid(row=0,column=2)
l3=Label(root,text="AM OR PM")
l3.grid(row=0,column=3)

btn=Button(root,text="set alarm",command=alarm)
btn.grid(row=2,column=2)

root.mainloop()