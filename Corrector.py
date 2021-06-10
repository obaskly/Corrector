from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
#pip install language-check
#pip install textblob
import language_check
from textblob import TextBlob


def root():
    global master
    master = Tk()
    master.resizable(FALSE, FALSE)
    master.title("اختبر انجليزيتك")
    #messagebox.showinfo("Notice !", ''.join('All Rights Reserved To Bropocalypse Team'))
    
    master.geometry("250x150")
    
    label0 = Label(master, 
                text ="V 1.0")
    
    label0.pack(pady = 10)

    btn0 = Button(master, 
                text ="اخطاء املائية", 
                command = win1)
    btn2 = Button(master, 
                text ="اخطاء نحوية", 
                command = win2)

    btn0.pack(pady = 7)
    btn2.pack(pady = 7)
    Quit = Button(master, text="Quit", command= lambda:[rem(), master.destroy()])
    Quit.place(x=0, y=125)

    mainloop()

def win1():
    win1 = Toplevel(master)
    win1.resizable(FALSE, FALSE)
    win1.title("اخطاء املائية")
    win1.geometry("250x150")
    win1.configure(background='black')
    #messagebox.showinfo("Notice !", ''.join('All Rights Reserved To Bropocalypse Team'))
    
    label1 = Label(win1, 
                text ="نصك :", background='black', foreground="red", font='Helvetica 9')

    label22 = Label(win1, 
                text ="التصحيح :", background='black', foreground="light green", font='Neutra 9')
                
    global e01, e10
    e01  = Entry(win1, width=25)
    e10  = Entry(win1, width=25)

    btn01 = Button(win1, 
                text ="تصحيح", 
                command = take)

    btn20 = Button(win1, 
                text ="خروج", 
                command = win1.destroy)

    label1.place(x=31, y=25)
    label22.place(x=20, y=55)

    e01.place(x=85, y=25)
    e10.place(x=85, y=55)

    btn01.place(x=90, y=85)
    btn20.place(x=90, y=115)
    
    win1.mainloop()

def win2():
    win2 = Toplevel(master)
    win2.resizable(FALSE, FALSE)
    win2.title("اخطاء نحوية")
    win2.geometry("250x150")
    win2.configure(background='black')
    #messagebox.showinfo("Notice !", ''.join('All Rights Reserved To Bropocalypse Team'))
    
    label15 = Label(win2, 
                text ="نصك :", background='black', foreground="red", font='Helvetica 9')

    label23 = Label(win2, 
                text ="التصحيح :", background='black', foreground="light green", font='Neutra 9')
                
    global e00, e11
    e00  = Entry(win2, width=25)
    e11  = Entry(win2, width=25)

    btn7 = Button(win2, 
                text ="تصحيح", 
                command = lol)

    btn8 = Button(win2, 
                text ="خروج", 
                command = win2.destroy)

    label15.place(x=31, y=25)
    label23.place(x=20, y=55)

    e00.place(x=85, y=25)
    e11.place(x=85, y=55)

    btn7.place(x=90, y=85)
    btn8.place(x=90, y=115)
    
    win2.mainloop()

def who(raw):
    pro = TextBlob(raw)
    return str(pro.correct())

def take():
    input = e01.get()
    fun = who(input)

    e10.delete(0,END)
    e10.insert(0,fun)

def grammar(text):
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)

    y = language_check.correct(text, matches)
    return y

def lol():
    input0 = e00.get()
    fun1 = grammar(input0)

    e11.delete(0,END)
    e11.insert(0,fun1)

def rem():
    messagebox.showinfo("تذكير", ''.join('لا تنسى مراجعة دروسك'))

root()
