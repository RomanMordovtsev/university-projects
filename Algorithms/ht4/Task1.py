stuffdict = {'couch_s': (300, 75),
             'couch_b': (500, 80),
             'bed': (400, 100),
             'closet': (200, 50),
             'bed_s': (200, 40),
             'desk': (200, 70),
             'table': (300, 80),
             'tv_table': (200, 30),
             'armchair': (100, 30),
             'bookshelf': (200, 60),
             'cabinet': (150, 20),
             'game_table': (150, 30),
             'hammock': (250, 45),
             'diner_table_with_chairs': (250, 70),
             'stools': (150, 30),
             'mirror': (100, 20),
             'instrument': (300, 70),
             'plant_1': (25, 10),
             'plant_2': (30, 20),
             'plant_3': (45, 25),
             'sideboard': (175, 30),
             'chest_of_drawers': (25, 40),
             'guest_bed': (250, 40),
             'standing_lamp': (20, 30),
             'garbage_can': (30, 35),
             'bar_with_stools': (200, 40),
             'bike_stand': (100, 80),
             'chest': (150, 25),
             'heater': (100, 25)
             }

def createTable(stuffdict, volume):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]

    n = len(value)

    table = [[0 for a in range(volume + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(volume + 1):
            if i == 0 or a == 0:
                table[i][a] = 0
            elif area[i - 1] <= a:
                table[i][a] = max(value[i - 1] + table[i - 1][a - area[i - 1]], table[i - 1][a])
            else:
                table[i][a] = table[i - 1][a]

    return table

def getItems(stuffdict, volume):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]

    table = createTable(stuffdict, 2000)
    a = volume
    n = len(value)
    res = table[-1][-1]

    items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][a]:
            continue
        else:
            items.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]
            a -= area[i - 1]

    selected_stuff = []

    for search in items:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)


    for i in selected_stuff:
        stuffdict.pop(i)

    return selected_stuff

print(getItems(stuffdict, 2000))


