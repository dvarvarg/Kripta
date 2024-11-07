from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import datetime


def update_result_label(event):
    # Обновляем метку результата (удаляем из нее предыдущие данные)
    result_label.config(text='')


def update_cur_label(event):
    # Получаем полное название валюты (в которую конвертируем) из словаря и обновляем метку
    result_label.config(text='')
    code=combobox_cur.get()
    name=cur[code]
    cur_label.config(text=name)


def exchange(event=None):
    # Получаем данные из выпадающих списков с валютой
    crypt_code=combobox_cript.get()
    cur_code=combobox_cur.get()
    # Получаем текущую дату и время
    now_dt = datetime.datetime.now().strftime('%d.%m.%Y %X')

    # Проверяем, выбраны ли пользователем данные из выпадающих списков. Если выбрано, то:
    if crypt_code and cur_code:
        try:
            # Отправляем GET-запрос с использованием requests.get()
            response=requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypt_code}&vs_currencies={cur_code}')
            # Проверяем успешность запроса (код ответа 200)
            response.raise_for_status()
            # Обрабатываем ответ
            json_resp=response.json()

            if json_resp:
                # Получаем результат в метку результата
                result=json_resp[crypt_code.lower()]
                result_label.config(text=f'Курс на {now_dt} \nза 1 {crypt_code} - {result[cur_code.lower()]} {cur_code}', fg='#00782D')
            else:
                # Если данные введены неверно (например, при ручном вводе)
                result_label.config(text='Такого кода валюты не существует')
        except Exception as e:
            # Обрабатываем исключения, если не удалось получить ответ с запрашиваемого сайта
            mb.showerror('Ошибка!',f'Произошла ошибка: {e}')
    else:
        # Обрабатываем данные (показываем предупреждение), если валюта не выбрана
        mb.showwarning('Внимание!', 'Введите код валюты!')


# Список популярных криптовалют
sp_cript=['Bitcoin','Ethereum','Ripple','Litecoin','Cardano']

# Словарь кодов валют и их полных названий
cur= {
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'RUB': 'Российский рубль'
    }


# Создание графического интерфейса
window=Tk()
window.title('Транскрипт')
window.geometry(f'420x200+{window.winfo_screenwidth()//2-210}+{window.winfo_screenheight()//2-100}')
window.iconbitmap('coins.ico')

# Создание и размещение виджетов
# Лейбл и выпадающий список криптовалют
Label(window, text='Выберите криптовалюту: ', font='Arial,10').grid(row=0, column=0, padx=5, pady=10)
combobox_cript=ttk.Combobox(window, value=sp_cript, font='Arial,10')
combobox_cript.grid(row=0, column=1, padx=5, pady=2)
combobox_cript.bind('<<ComboboxSelected>>', update_result_label)

# Лейбл и выпадающий список валют
Label(window, text='Конвертировать в: ', font='Arial,10').grid(row=1, column=0, padx=5, pady=2)
combobox_cur=ttk.Combobox(window, value=list(cur.keys()), font='Arial,10')
combobox_cur.grid(row=1, column=1, padx=5, pady=2)
combobox_cur.bind('<<ComboboxSelected>>', update_cur_label)

# Метка для полного названия валюты, в которую конвертируем
cur_label=ttk.Label(window, font='Arial,10')
cur_label.grid(row=2, column=1, padx=5, pady=5)

# Кнопка вывода результата конвертации
targ_btn=Button(window, text='Получить курс', command=exchange, font='Arial,10', activebackground='#FF6140')
targ_btn.grid(row=3, column=1, columnspan=1, sticky='ew', padx=5, pady=5)
# Вывод результата конвертации с помощью кнопки Enter
window.bind('<Return>', exchange)

# Лейбл с результатом операции
result_label=Label(window, text='Выберите криптовалюту и валюту', font='Arial,10')
result_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

# Запуск главного цикла окна
window.mainloop()
