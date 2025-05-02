K3120 = {'Иванова Анастасия': ["чай", "коты", "кофе", "рыжие"],
         'Шевченко Кристина': ["кофе", "чай", "темные", "крашеные"],
         'Мордовцев Роман': ["чай", "коты", "кофе", "собаки", "светлые", "крашеные"],
         'Мартынюк Алексей': ["коты", "кофе", "спорт", "темные"],
         'Федорова Алина': ["чай", "коты", "спорт", "алкоголь", "темные"],
         'Цветкова Надежда': ["чай", "кофе", "спорт", "собаки", "светлые"],
         'Колтунова Полина': ["чай", "спорт", "темные"],
         'Никифоров Савелий': ["чай", "кофе", "спорт", "собаки", "алкоголь", "курение", "светлые"],
         'Резкаллах Кироллос': ["темные", "коты", "кофе"],
         'Морозова Яна': ["чай", "коты", "светлые", "очки"],
         'Гаджиева Патина': ["чай", "темные", "очки"],
         'Бахтина Анастасия': ["чай", "коты", "спорт", "собаки", "темные"],
         'Шапиро Михаил': ["коты", "кофе", "спорт", "алкоголь", "права", "темные"],
         'Зубкова Дарья': ["чай", "темные"],
         'Абдалла Мустафа': ["чай", "кофе", "темные", "коты"],
         'Агаев Хамза': ["чай", "кофе", "темные", "очки"],
         'Луценко Владимир': ["кофе", "алкоголь", "курение", "собаки"],
         'Мигулян Денис': ["кофе", "светлые", "коты", "собаки", "алкоголь"],
         'Сидненко Дмитрий': ["чай", "темные", "собаки", "кофе"],
         'Морозов Матвей': ["чай", "собаки", "алкоголь", "темные", "очки"],
         'Шимченко Александра': ["чай", "коты", "кофе", "собаки", "темные"],
         'Гуренков Максим': ["чай", "коты", "спорт", "курение", "темные"],
         'Ершов Николай': ["чай", "коты", "права", "темные"],
         'Шабанов Роман': ["темные", "коты", "кофе", "алкоголь", "курение"],
         'Уразалин Амир': ["коты", "кофе", "собаки", "темные", "очки"],
         'Скворцов Иван': ["чай", "коты", "кофе", "темные", "очки"],
         'Гусев Ярослав': ["чай", "коты", "кофе", "спорт", "собаки", "алкоголь", "темные"],
         'Коломиец Алиса': ["кофе", "чай", "светлые", "крашеные"],
         'Георгов Олег': ["кофе", "светлые", "крашеные", "очки"],
         'Мыльченко Алексей': ["чай", "собаки", "алкоголь", "светлые"]}

def Uga(group):
    c1 = input('Студент любит кофе? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not('кофе' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'кофе' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент любит котов и кошек? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('коты' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'коты' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент пьет? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('алкоголь' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'алкоголь' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('У студента светлые волосы? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('светлые' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'светлые' in group[i]:
                del group[i]
        if len(group) <= 1:
            for i in group:
                return list(group.keys())[list(group.values()).index(group[i])]
        c2 = input('У студента рыжие волосы? ')
        pod = group.copy()
        if c2 == 'Да':
            for i in pod:
                if not ('рыжие' in group[i]):
                    del group[i]
        else:
            for i in pod:
                if 'рыжие' in group[i]:
                    del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент курит? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('курение' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'курение' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент любит чай? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('чай' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'чай' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент носит очки? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('очки' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'очки' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент любит собак? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('собаки' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'собаки' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'
    c1 = input('Студент занимается спортом? ')
    pod = group.copy()
    if c1 == 'Да':
        for i in pod:
            if not ('спорт' in group[i]):
                del group[i]
    else:
        for i in pod:
            if 'спорт' in group[i]:
                del group[i]
    if len(group) <= 1:
        for i in group:
            return list(group.keys())[list(group.values()).index(group[i])]
    if len(list(group.keys())) == 0:
        return 'Такого студента в группе нет'



print(Uga(K3120))