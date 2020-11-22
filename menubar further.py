from tkinter import *




root=Tk()
root.geometry("650x650")
root.maxsize(650,650)
root.title("Simple Calculator_hs ")

root.configure(background="#defafb")

def click(event):
    global inp
    text=event.widget.cget('text')
    if text=="=":

        if inp.get().isdigit():
            value=int(inp.get())
        else:
            try:

                value=eval(g.get())



            except Exception  as e:
                print(e)
                value=f"Fuck off invalid syntext \U0001F923"

                g.update()
        inp.set(value)
        g.update()
    elif text=="C":
        inp.set("")
        g.update()
    else:
     inp.set(inp.get()+text)
     g.update()




inp=StringVar()

g=Entry(root,textvariable=inp,width=600,font="lucida 30 bold",justify=RIGHT,state=DISABLED,fg="#ec6d10")
g.pack(padx=10,pady=20)
f1=Frame(root,bg="#defafb")

b1=Button(f1,text='9',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b1.pack(side=LEFT,padx=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text='8',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b2.pack(side=LEFT,padx=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text='7',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b3.pack(side=LEFT,padx=10)
b3.bind("<Button-1>",click)
b4=Button(f1,text='+',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b4.pack(side=LEFT,padx=10)
b4.bind("<Button-1>",click)
b5=Button(f1,text='-',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b5.pack(side=LEFT,padx=10)
b5.bind("<Button-1>",click)
f1.pack()

f2=Frame(root,bg="#defafb")
b1=Button(f2,text='6',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)
b2=Button(f2,text='5',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b2.pack(side=LEFT,padx=10,pady=5)
b2.bind("<Button-1>",click)
b3=Button(f2,text='4',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b3.pack(side=LEFT,padx=9,pady=5)
b3.bind("<Button-1>",click)
b4=Button(f2,text='*',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b4.pack(side=LEFT,padx=10,pady=5)
b4.bind("<Button-1>",click)
b5=Button(f2,text='/',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=28,pady=28)
b5.pack(side=LEFT,padx=10)
b5.bind("<Button-1>",click)
f2.pack()

f3=Frame(root,bg="#defafb")
b1=Button(f3,text='1',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=26,pady=28)
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)
b2=Button(f3,text='2',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=26,pady=28)
b2.pack(side=LEFT,padx=10,pady=5)
b2.bind("<Button-1>",click)
b3=Button(f3,text='3',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=26,pady=28)
b3.pack(side=LEFT,padx=10,pady=5)
b3.bind("<Button-1>",click)
b4=Button(f3,text='.',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=30,pady=28)
b4.pack(side=LEFT,padx=0,pady=5)
b4.bind("<Button-1>",click)
b5=Button(f3,text='%',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=26,pady=28)
b5.pack(side=LEFT,padx=10)
b5.bind("<Button-1>",click)
f3.pack()


f4=Frame(root,bg="#defafb")
b1=Button(f4,text='C',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=26,pady=28)
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)
b2=Button(f4,text='0',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=30,pady=28,width=2)
b2.pack(side=LEFT,padx=12,pady=5)
b2.bind("<Button-1>",click)
b3=Button(f4,text='00',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=60,pady=28)
b3.pack(side=LEFT,padx=8,pady=5)
b3.bind("<Button-1>",click)

b5=Button(f4,text='=',font="arial 25 bold",bd=2,relief=SUNKEN,bg="#e3dbff",padx=30,pady=28)
b5.pack(side=LEFT,padx=25)
b5.bind("<Button-1>",click)
f4.pack()


root.mainloop()