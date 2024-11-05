from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import datetime


def update_cur_label(event):
    code=combobox_cur.get()
    name=cur[code]
    cur_label.config(text=name)


def exchange():
    crypt_code=combobox_cript.get()
    cur_code=combobox_cur.get()
    now_dt = datetime.datetime.now().strftime('%d.%m.%Y %X')

    if crypt_code and cur_code:
        try:
            response=requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypt_code}&vs_currencies={cur_code}')
            response.raise_for_status() # Проверка на ошибки
            json_resp=response.json()

            if json_resp:
                result=json_resp[crypt_code.lower()]
                result_label.config(text=f'Курс на {now_dt}:\n за 1 {crypt_code} - {result[cur_code.lower()]} {cur_code}', fg='#00782D')
            else:
                result_label.config(text='Такого кода валюты не существует')
        except Exception as e:
            mb.showerror('Ошибка!',f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')


sp_cript=['Bitcoin','Ethereum','Ripple','Litecoin','Cardano']

cur= {
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'RUB': 'Российский рубль'
    }


window=Tk()
window.title('Криптовалюта')
window.geometry(f'420x200+{window.winfo_screenwidth()//2-210}+{window.winfo_screenheight()//2-100}')
window.iconbitmap('coins.ico')

# лейбл и выпадающий список криптовалют
Label(text='Выберите криптовалюту: ', font='Arial,10').grid(row=0,column=0,padx=5, pady=10)
combobox_cript=ttk.Combobox(window,value=sp_cript, font='Arial,10')
combobox_cript.grid(row=0,column=1,padx=5, pady=2)

# выпадающий список валют
Label(text='Выберите валюту: ', font='Arial,10').grid(row=1,column=0,padx=5, pady=2)
combobox_cur=ttk.Combobox(value=list(cur.keys()), font='Arial,10')
combobox_cur.grid(row=1,column=1,padx=5, pady=2)
combobox_cur.bind('<<ComboboxSelected>>',update_cur_label)

cur_label=ttk.Label(font='Arial,10')
cur_label.grid(row=2,column=1,padx=5, pady=5)

# кнопка вывода
targ_btn=Button(window, text='Получить курс',command=exchange, font='Arial,10')
targ_btn.grid(row=3,column=1,columnspan=1,sticky='ew',padx=5, pady=5)

# лейбл с результатом операции
result_label=Label(text='Выберите криптовалюту и валюту', font='Arial,10')
result_label.grid(row=4,column=0, columnspan=2,sticky='ew',padx=5, pady=5)

window.mainloop()