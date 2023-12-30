from tkinter import *
from tkinter.ttk import *

from time import strftime

bar = Tk()
bar.title('DIGITAL TIME')

def time():
    String = strftime('%m-%d-%y:%H:%M:%S %p')
    label.config(text=String)
    label.after(1000, time)

label = Label(bar, font=('Times New Romans', 50), background='skyblue', foreground='blue')
label.pack(anchor='center')


time()    
mainloop()
