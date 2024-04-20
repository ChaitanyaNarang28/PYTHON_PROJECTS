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

nvalue=9

for i in range(0,3):
    f1=Frame(root,bg="grey")
    for j in range(0,3):
        b9=Button(f1,text=str(nvalue),font='lucida 20 bold',padx=28,pady=18)
        b9.pack(side=LEFT,padx=18,pady=5)
        b9.bind("<Button-1>",click)
        nvalue=nvalue-1
        
    f1.pack()

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
