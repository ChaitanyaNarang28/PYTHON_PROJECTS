from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os 
def nfile():
    global file
    root.title("Untitled-Notepad")
    print("File created")
    print("Hiii","Bye")
    file=None
    textarea.delete(1.0,END)

def ofile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documnets","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        
def sfile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documnets","*.txt")])
    
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad") 
            print("File Saved")
        
    else:
        f=open(file,'w')
        f.write(textarea.get(1.0,END))
        f.close()
    

def close():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad By Chaitanya Narang")


if __name__=='__main__':
    root=Tk()
    root.geometry('450x600')

    #TO  CREATE TEXT AREA
    textarea=Text(root,font="Lucidia 13")
    file=None
    textarea.pack(fill=BOTH,expand=True)
    
    #TO  CREATE A MENU BAR
    menu_bar=Menu(root)
    
    file_menu=Menu(menu_bar,tearoff=0)
    #TO  OPEN A NEW FILE (MENU BAR)
    file_menu.add_command(label="New",command=nfile)
    #TO  OPEN AN EXISTING FILE
    file_menu.add_command(label="Open",command=ofile)
    #TO  SAVE A FILE
    file_menu.add_command(label="Save",command=sfile)
    file_menu.add_separator()
    #TO  EXIT
    file_menu.add_command(label="Exit",command=close)

    menu_bar.add_cascade(label='File',menu=file_menu)
    root.config(menu=menu_bar)
    
    edit_menu=Menu(menu_bar,tearoff=0)
    #TO  OPEN A NEW FILE (MENU BAR)
    edit_menu.add_command(label="Cut",command=cut)
    #TO  OPEN AN EXISTING FILE
    edit_menu.add_command(label="Copy",command=copy)
    #TO  SAVE A FILE
    edit_menu.add_command(label="Paste",command=paste)
    
    menu_bar.add_cascade(label='Edit',menu=edit_menu)
    root.config(menu=menu_bar)
    
    
    help_menu=Menu(menu_bar,tearoff=0)
    #TO  OPEN A NEW FILE (MENU BAR)
    help_menu.add_command(label="About",command=about)

    menu_bar.add_cascade(label='help',menu=help_menu)
    root.config(menu=menu_bar)
    
    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    
    root.mainloop()