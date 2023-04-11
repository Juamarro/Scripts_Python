import tkinter as tk
from tkinter import *

import ttkbootstrap as tb


from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from PIL import Image, ImageTk
from ttkbootstrap.scrolled import ScrolledFrame


import time

def mostrar_info():
    info_window = tk.Toplevel(root)
    info_label = tk.Label(info_window, text="Aquí va tu información")


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Progress Bars")

root.geometry('1000x800')

# Increment 20
def increment():
    #my_progress.step(20)
    my_progress['value'] += 20
    # Get current value
    my_label.config(text=my_progress['value'])

# Progress Bar
my_progress = tb.Progressbar(root, bootstyle='success striped', 
    maximum=100, 
    mode="determinate",
    length=800, 
    value=0)

my_progress.place(relx=0.08,rely=0.02)

# Buttons
my_button = tb.Button(root, text="Increment 20", bootstyle="info", command=increment)
my_button.place(relx=0.08,rely=0.06)

b1 = tb.Button(root, text='primary', bootstyle=PRIMARY)
b1.place(relx=0.10,rely=0.15,width=70)

b1 = tb.Button(root, text='primary', bootstyle=PRIMARY)
b1.place(relx=0.7,rely=0.18,width=70)


# Create a label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.place(relx=0.89,rely=0.013)

#Frame 1

my_label1 = tb.Labelframe(root,text='Modelo')
my_label1.place(relx=0.07,rely=0.15)
my_label1.config(width=800,height=120)

my_meter = tb.Meter(my_label1, bootstyle="Success", 
    textright="%",
    metertype="full", # Can be semi
    metersize=100,
    amountused=0,
    amounttotal=100,
    subtextstyle="light"
    )
my_meter.place(relx=0,rely=0.0)

my_label2 = tb.Label(my_label1, text="Porcentaje", font=("Helvetica", 18))
my_label2.place(relx=0.12,rely=0.3)

my_meter1 = tb.Meter(my_label1, bootstyle="Success", 
    textright="%",
    metertype="full", # Can be semi
    metersize=100,
    amountused=0,
    amounttotal=100,
    textfont=10 ,
    subtextstyle="light"
    )
my_meter1.place(relx=0.4,rely=0)

my_label3 = tb.Label(my_label1, text="Porcentaje", font=("Helvetica", 18))
my_label3.place(relx=0.52,rely=0.3)

boton = tk.Button(root, text="Mostrar información", command=mostrar_info)
boton.pack()

increment()

root.update()

root.mainloop()