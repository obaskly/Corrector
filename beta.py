from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#pip install textblob
from textblob import TextBlob

def root():
    global master
    master = Tk()
    master.resizable(FALSE, FALSE)
    master.title("اختبر انجليزيتك")
    master.geometry("250x150")
    master.configure(background='black')
    #messagebox.showinfo("Notice !", ''.join('All Rights Reserved To Bropocalypse Team'))
    
    label = Label(master, 
                text ="نصك :", background='black', foreground="red", font='Helvetica 9')

    label2 = Label(master, 
                text ="التصحيح :", background='black', foreground="light green", font='Neutra 9')
                
    global e0, e1
    e0  = Entry(master, width=25)
    e1  = Entry(master, width=25)

    btn = Button(master, 
                text ="تصحيح", 
                command = take)

    btn2 = Button(master, 
                text ="خروج", 
                command = lambda:[rem(), master.destroy()])

    label.place(x=31, y=25)
    label2.place(x=20, y=55)

    e0.place(x=85, y=25)
    e1.place(x=85, y=55)

    btn.place(x=90, y=85)
    btn2.place(x=90, y=115)
    
    mainloop()
    
def who(raw):
    pro = TextBlob(raw)
    return str(pro.correct())

def take():
    input = e0.get()
    fun = who(input)

    e1.delete(0,END)
    e1.insert(0,fun)

def rem():
    messagebox.showinfo("تذكير", ''.join('لا تنسى مراجعة دروسك'))

root()