from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import File_writing as fi
from tkinter import messagebox
import File_open as fo

def get_info():
    name = entry1.get()
    surname = entry2.get()
    description = entry2.get()
    info = []
    info.append(name)
    info.append(surname)

    try:
        phone_number = entry3.get()
        if len(phone_number) != 11:
            messagebox.showwarning(title="Ошибка", message="В номере телефона должно быть 11 цифр")
        else:
            phone_number = int(phone_number)
    except:
        messagebox.showwarning(title="Ошибка", message="В номере телефона доблжны быть только цифры")
    info.append(phone_number)
    info.append(description)
    return info

def add_info():
    fi.writing_txt(get_info())
    fi.writing_scv (get_info())
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

def get_txt():
    text = fo.open_txt()
    txt.delete(1.0, END)
    txt.insert(INSERT, text)

def get_csv():
    text = fo.open_csv()
    txt.delete(1.0, END)
    txt.insert(INSERT, text)

root = Tk()
root.title("Телефонная книга")
root.geometry("450x550") 


label1 = ttk.Label(root, text="Фамилия").pack(anchor=NW, padx=6, pady=0)
entry1 = ttk.Entry()
entry1.pack(anchor=NW, padx=6, pady=6,)

label2 = ttk.Label(root, text="Имя").pack(anchor=NW, padx=6, pady=0)
entry2 = ttk.Entry()
entry2.pack(anchor=NW, padx=6, pady=6)

label3 = ttk.Label(root, text="Телефон").pack(anchor=NW, padx=6, pady=0)
entry3 = ttk.Entry()
entry3.pack(anchor=NW, padx=6, pady=6)

label4 = ttk.Label(root, text="Описание").pack(anchor=NW, padx=6, pady=0)
entry4 = ttk.Entry()
entry4.pack(anchor=NW, padx=6, pady=6)
  
btn1 = ttk.Button(text="Добавить", command=add_info)
btn1.pack(anchor=NW, padx=6, pady=6)

txt = scrolledtext.ScrolledText(root, width=40, height=10)  
txt.pack(anchor=W, ipadx=5, ipady=5)

btn2 = ttk.Button(text="Открыть txt", command=get_txt)
btn2.pack(anchor=NW, padx=6, pady=6, side=LEFT)
btn2 = ttk.Button(text="Открыть csv", command=get_csv)
btn2.pack(anchor=NW, padx=6, pady=6)

def start():   
    root.mainloop()