from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests

def upload():
    filepath =fd.askopenfilename()
    if filepath:
        files = {"file":open(filepath,"rd")}
        response = requests.post("http://file.io",files=files)
        if response.status_code==200:
            link =response.json()["link"]
            entry.insert(0,link)

window=Tk()
window.title("Сохранение файла")
window.geometry("400x200")


button=ttk.Button(text= "Загрузить файл",command=upload)
button.pack()



entry =ttk.Entry()
entry.pack()

window.main.loop()

