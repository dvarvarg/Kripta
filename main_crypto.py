from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

sp_cript=['Bitcoin','Ethereum','Ripple USD','Litecoin','Cardano']


window=Tk()
window.title('Криптовалюта')
window.geometry(f'400x200+{window.winfo_screenwidth()//2-200}+{window.winfo_screenheight()//2-100}')
window.iconbitmap('coins.ico')

combo=ttk.Combobox(window,value=sp_cript)
combo.pack()

targ_btn=Button(window, text='Получить курс')
targ_btn.pack()

rez_label=Label(text='')
rez_label.pack()




window.mainloop()