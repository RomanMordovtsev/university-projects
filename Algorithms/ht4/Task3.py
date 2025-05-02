import random
array = [random.randint(1, 100) for i in range(30)]


max_i = 0
cur_i = 0

for i in range(1, len(array)):
    if array[i] >= array[i-1]:
        cur_i += 1

    else:
        if max_i < cur_i:
            max_i = cur_i
            cur_i = 0

print(max_i)
