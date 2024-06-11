from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
                # scvalue.set("Error")
                # screen.update()
        
        scvalue.set(value)
        screen.update()
            
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry('600x800')

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font='lucida 40 bold')
screen.pack(fill=X,ipadx=18,pady=10,padx=30 )

f1=Frame(root,bg="grey")
b9=Button(f1,text="9",font='lucida 20 bold',padx=28,pady=18)
b9.pack(side=LEFT,padx=18,pady=5)
b9.bind("<Button-1>",click)

b8=Button(f1,text="8",font='lucida 20 bold',padx=28,pady=18)
b8.pack(side=LEFT,padx=18,pady=5)
b8.bind("<Button-1>",click)

b7=Button(f1,text="7",font='lucida 20 bold',padx=28,pady=18)
b7.pack(side=LEFT,padx=18,pady=5)
b7.bind("<Button-1>",click)

f1.pack()

f2=Frame(root,bg="grey")
b6=Button(f2,text="6",font='lucida 20 bold',padx=28,pady=18)
b6.pack(side=LEFT,padx=18,pady=5)
b6.bind("<Button-1>",click)

b5=Button(f2,text="5",font='lucida 20 bold',padx=28,pady=18)
b5.pack(side=LEFT,padx=18,pady=5)
b5.bind("<Button-1>",click)

b4=Button(f2,text="4",font='lucida 20 bold',padx=28,pady=18)
b4.pack(side=LEFT,padx=18,pady=5)
b4.bind("<Button-1>",click)

f2.pack()


f3=Frame(root,bg="grey")
b3=Button(f3,text="3",font='lucida 20 bold',padx=28,pady=18)
b3.pack(side=LEFT,padx=18,pady=5)
b3.bind("<Button-1>",click)

b2=Button(f3,text="2",font='lucida 20 bold',padx=28,pady=18)
b2.pack(side=LEFT,padx=18,pady=5)
b2.bind("<Button-1>",click)

b1=Button(f3,text="1",font='lucida 20 bold',padx=28,pady=18)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

f3.pack( )


f4=Frame(root,bg="grey")
b11=Button(f4,text="0",font='lucida 20 bold',padx=28,pady=18)
b11.pack(side=LEFT,padx=18.5,pady=5)
b11.bind("<Button-1>",click)

b5=Button(f4,text="-",font='lucida 20 bold',padx=28,pady=18)
b5.pack(side=LEFT,padx=18.5,pady=5)
b5.bind("<Button-1>",click)

b13=Button(f4,text="+",font='lucida 20 bold',padx=28,pady=18)
b13.pack(side=LEFT,padx=18.5,pady=5)
b13.bind("<Button-1>",click)

f4.pack()

f5=Frame(root,bg="grey")
b14=Button(f5,text="*",font='lucida 20 bold',padx=28,pady=18)
b14.pack(side=LEFT,padx=18.5,pady=5)
b14.bind("<Button-1>",click)

b15=Button(f5,text="/",font='lucida 20 bold',padx=28,pady=18)
b15.pack(side=LEFT,padx=18,pady=5)
b15.bind("<Button-1>",click)

b16=Button(f5,text="%",font='lucida 20 bold',padx=27.5,pady=18)
b16.pack(side=LEFT,padx=18.5,pady=5)
b16.bind("<Button-1>",click)

f5.pack()

f6=Frame(root,bg="grey")
b19=Button(f6,text=".",font='lucida 20 bold',padx=28,pady=18)
b19.pack(side=LEFT,padx=18.4,pady=5)
b19.bind("<Button-1>",click)


b17=Button(f6,text="=",font='lucida 20 bold',padx=28,pady=18)
b17.pack(side=LEFT,padx=18.5,pady=5)
b17.bind("<Button-1>",click)

b18=Button(f6,text="C",font='lucida 20 bold',padx=28,pady=18)
b18.pack(side=LEFT,padx=18,pady=5)
b18.bind("<Button-1>",click)

f6.pack()

root.mainloop()
