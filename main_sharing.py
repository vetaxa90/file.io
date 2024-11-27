from tkinter import *
import requests
from tkinter import filedialog as fd


win=Tk()

win.title("Обмен файлами")
win.geometry("500x300")



Label(win,text="Путь к файлу",font=("Comic Sans MS",14))
Button(win,text="выбрать файл",font=("Comic Sans MS",14)).pack()

e =Entry(win,font=("Comic Sans MS",12))
e.pack()

win.mainloop()