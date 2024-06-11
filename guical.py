from tkinter import *
def click(event):
    global scvalue
    text= event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value =int(scvalue.get())
        else:
             try:
                 value= eval(screen.get()) 
             except Exception as e:
                 print(e)
                 value = "Error"

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    
    elif text=="AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
root=Tk()
root.geometry("745x950")
root.title("Calculator With Priya Gupta")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=10,pady=10)

f=Frame(root,bg="grey")
b=Button(f,text="=",padx=35,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=35,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=35,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=35,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="*",padx=38,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="9",padx=37,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=37,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=38,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="-",padx=37.5,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=38,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=38,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="6",padx=38,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="+",padx=35,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=37,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=37,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="3",padx=37,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="00",padx=29.5,pady=22,font="lucida 35 bold")
b.pack(side="right",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="AC",padx=30,pady=22,font="lucida 35 bold")
b.pack(side="left",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=30,pady=22,font="lucida 35 bold")
b.pack(side="left",padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=30,pady=22,font="lucida 35 bold")
b.pack(side="left",padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()


root.mainloop()