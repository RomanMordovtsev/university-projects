import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry # Для удобного формата записи даты
import tkinter.messagebox as mb # Для вывода ошибки при вводе данных

ws = tk.Tk()
ws.title('Контроль денежных средств')
# Создание использующихся фреймов
frame_b = tk.Frame(ws)
frame_b.grid(row=0, column=0)
frame = tk.Frame(ws)
frame.grid(row=1, column=0)

# Начальные данные
things = [
    ["Хлеб", "Еда", "30", "2022.12.05"],
    ["Пижама", "Одежда", "800", "2019.12.01"],
    ["Тринадцатая сказка", "Книги", "300", "2021.01.20"]
]

#Категории

cats = ["Еда", "Одежда", "Техника", "Для дома", "Для творчества", "Канцелярия", "Настольные игры", "Книги", "Остальное"]

# Заголовки таблицы

headlines = ["Продукт", "Категория", "Цена (в рублях)", "Дата покупки"]

# Функция для ввода новых данных пользователем

navsyak = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def Input_record():
    if len(name_use.get()) < 25 and len(category_use.get()) < 25 and len(price_use.get()) < 25 and len(date_use.get()) < 25 \
            and set(map(str, category_use.get())) & navsyak == set() and set(map(str, price_use.get())) <= navsyak:
        table.insert(parent='', index='end', text='', values=(name_use.get(), category_use.get(),
                                                                         price_use.get(), date_use.get()))
    else:
        mb.showerror('Ошибка', 'Недопустимый формат ввода')

# Инстурументы для ввода данных
name = ttk.Label(frame_b, text='Введите продукт')
name.grid(row=0, column=0, sticky='w', padx=10, pady=5)
name_use = ttk.Entry(frame_b, justify=tk.LEFT)
name_use.grid(row=0, column=1, sticky='e', padx=10, pady=5)
category = ttk.Label(frame_b, text='Выберите категорию продукта')
category.grid(row=1, column=0, sticky='w', padx=10, pady=5)
category_use = ttk.Combobox(frame_b, values=cats)
category_use.grid(row=1, column=1, sticky='e', padx=10, pady=5)
price = ttk.Label(frame_b, text='Введите цену')
price.grid(row=2, column=0, sticky='w', padx=10, pady=5)
price_use = ttk.Entry(frame_b, justify=tk.LEFT)
price_use.grid(row=2, column=1, sticky='e', padx=10, pady=5)
date = ttk.Label(frame_b, text='Введите дату')
date.grid(row=3, column=0, sticky='w', padx=10, pady=5)
date_use = DateEntry(frame_b, date_pattern='YYYY.mm.dd')
date_use.grid(row=3, column=1, sticky='e', padx=10, pady=5)
btn_update = ttk.Button(frame_b, text='Добавить продукт', command=Input_record)
btn_update.grid(row=4, column=0, columnspan=2)

# Ввод таблицы
table = ttk.Treeview(frame, show='headings')
table['columns'] = headlines

# Функция для сортировки данных

def table_sort_column(table, header, reverse):
    try:
        l = [(int(table.set(k, header)), k) for k in table.get_children('')]
    except Exception:
        l = [(table.set(k, header), k) for k in table.get_children('')]
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        table.move(k, '', index)

    table.heading(header, command=lambda _header=header: table_sort_column(table, _header, not reverse))

# Циклы, добавляющие данные в таблицу

for header in headlines:
    table.heading(header, text=header, anchor='center', command=lambda _header=header: table_sort_column(table, _header,
                                                                                                         False))
    table.column(header, anchor='center')

for row in things:
    table.insert('', tk.END, values=row)

# Добавление возможности скроллить

scroll = ttk.Scrollbar(frame, command=table.yview)
table.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

table.pack()

# Удаление элемента из таблицы

def remove_one():
    x = table.selection()[0]
    table.delete(x)

btn = tk.Button(frame, text='Удалить запись', command=remove_one)
btn.pack()


ws.mainloop()
