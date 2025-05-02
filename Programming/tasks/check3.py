import tkinter as tk
from tkinter import messagebox


class FightingApp: # Создание класса для визуализации
    def __init__(self, master):
        self.master = master # Основное окно приложения
        master.title('Fighting Game') # Заголовок

        self.fighter1_label = tk.Label(master, text='Fighter 1:') # Ввод данных о бойцах
        self.fighter1_label.grid(row=0, column=0)
        self.fighter1_name_label = tk.Label(master, text='Name:')
        self.fighter1_name_label.grid(row=1, column=0)
        self.fighter1_name_entry = tk.Entry(master)
        self.fighter1_name_entry.grid(row=1, column=1)
        self.fighter1_health_label = tk.Label(master, text='Health:')
        self.fighter1_health_label.grid(row=2, column=0)
        self.fighter1_health_entry = tk.Entry(master)
        self.fighter1_health_entry.grid(row=2, column=1)

        self.fighter2_label = tk.Label(master, text='Fighter 2:')
        self.fighter2_label.grid(row=3, column=0)
        self.fighter2_name_label = tk.Label(master, text='Name:')
        self.fighter2_name_label.grid(row=4, column=0)
        self.fighter2_name_entry = tk.Entry(master)
        self.fighter2_name_entry.grid(row=4, column=1)
        self.fighter2_health_label = tk.Label(master, text='Health:')
        self.fighter2_health_label.grid(row=5, column=0)
        self.fighter2_health_entry = tk.Entry(master)
        self.fighter2_health_entry.grid(row=5, column=1)

        self.start_button = tk.Button(master, text='Start Fight', command=self.start_fight) # Кнопка для того, чтобы начать поединок
        self.start_button.grid(row=6, column=1)

        self.fight_results = tk.Text(master, height=10, width=40) # Создание тектового виджета для отображения информации о ходе боя
        self.fight_results.grid(row=7, column=0, columnspan=2)

    def start_fight(self):
        # Собирание значений первого бойца
        fighter1_name = self.fighter1_name_entry.get()
        fighter1_health = int(self.fighter1_health_entry.get())
        # Проверка на пустые поля
        if fighter1_name == '' or fighter1_health == '':
            messagebox.showwarning('Error', 'Please fill in all fields for Fighter 1.')
            return
        # Собирание значений второго бойца
        fighter2_name = self.fighter2_name_entry.get()
        fighter2_health = int(self.fighter2_health_entry.get())
        # Проверка на пустые поля
        if fighter2_name == '' or fighter2_health == '':
            messagebox.showwarning('Error', 'Please fill in all fields for Fighter 2.')
            return
        # Начало боя
        self.fight_results.delete('1.0', tk.END)
        self.fight_results.insert(tk.END, f'{fighter1_name} vs. {fighter2_name}\n')
        self.fight_results.insert(tk.END, 'FIGHT!\n')
        while fighter1_health > 0 and fighter2_health > 0:
            # Атака первого бойца
            attack1 = max(1, fighter1_health // 10)
            fighter2_health -= attack1
            self.fight_results.insert(tk.END, f'{fighter1_name} attacks {fighter2_name} for {attack1} damage. '
                                              f'{fighter2_name} now has {fighter2_health} health.\n')
            # Проверка на жизненное состояние
            if fighter2_health <= 0:
                self.fight_results.insert(tk.END, f'{fighter1_name} wins!\n')
                break
            # Атака второго бойца
            attack2 = max(1, fighter2_health // 10)
            fighter1_health -= attack2
            self.fight_results.insert(tk.END, f'{fighter2_name} attacks {fighter1_name} for {attack2} damage. '
                                              f'{fighter1_name} now has {fighter1_health} health.\n')
            # Проверка на жизненное состояние
            if fighter1_health <= 0:
                self.fight_results.insert(tk.END, f'{fighter2_name} wins!\n')
                break

# Запуск графического интерфейса (при условии, что проект исполняется в "main")
if __name__ == '__main__':
    root = tk.Tk()
    app = FightingApp(root)
    root.mainloop()
