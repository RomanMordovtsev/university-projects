from random import randint

cash = {}                               # ключ - цена монеты, значение - количество монеты

for i in range(4):                      # генерируем монеты
    coin = randint(1, 10)
    count = randint(1, 10)
    while coin in cash.keys():
        coin = randint(1, 10)
    cash[coin] = count


total_cash = 0
for i in cash:                          # общая сумма все имеющихся монет
    total_cash += i * cash[i]
print(cash)

N = randint(1, total_cash)              # сумма, которую надо выдать

summ = 0

gived = []                              # монеты, которые были выданы
while summ < N:
    moneys = list(reversed(sorted(cash.keys())))
    i = 0
    while i < len(moneys):
        if (moneys[i] <= (N - summ)) and cash[moneys[i]] != 0:
            cash[moneys[i]] -= 1
            summ += moneys[i]
            gived.append(moneys[i])
            break
        i += 1
    if i == len(moneys):
        for i in reversed(moneys):
            if cash[i] != 0:
                summ += i
                gived.append(i)
                break

print(f"Сумма, которую надо выдать: {N}")
print(f"Выданная сумма: {summ}\nМонеты, которые были выданы: {gived}")


