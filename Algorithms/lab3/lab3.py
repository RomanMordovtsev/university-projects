from random import randint
import timeit

# Task 1
nums = [randint(-100, 100) for i in range(10)]
def bubble(nums):
    for i in range(len(nums)-1):
       for j in range(len(nums)-1 - i):
           if nums[j] > nums[j + 1]:
               nums[j], nums[j+1] = nums[j + 1], nums[j]
    return nums

def bubble():
    nums = [randint(-100, 100) for i in range(10)]
    for i in range(len(nums)-1):
       for j in range(len(nums)-1 - i):
           if nums[j] > nums[j + 1]:
               nums[j], nums[j+1] = nums[j + 1], nums[j]
    return nums

def sssor():
    nums = [randint(-100, 100) for i in range(10)]
    return nums.sort()

#print(timeit.timeit(bubble, number=1))
#print(timeit.timeit(sssor, number=1))

# Task 2

def linear(nums):
    div_0 = 0
    div_1 = 0
    div_2 = 0
    for i in nums:
        if i % 3 == 0:
            div_0 += 1
    for j in nums:
        if j % 3 == 1:
            div_1 += 1
    for k in nums:
        if k % 3 == 2:
            div_2 += 1
    return div_0, div_1, div_2

#print(nums, linear(nums))

def merge(nums):
    n = len(nums)
    if n > 1:
        mid = n//2
        left = nums[:mid]
        right = nums[mid:]
        merge(left)
        merge(right)
        l = 0
        k = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[k] = left[l]
                l += 1
            else:
                nums[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            nums[k] = left[l]
            k += 1
            l += 1
        while r < len(right):
            nums[k] = right[r]
            r += 1
            k += 1
    return nums

#print(nums)
#print(merge(nums))

def factorial(nums):
    summa = 0
    k = 0
    while k < len(nums):
        for i in range(k, len(nums)):
            summa += nums[i]
        k += 1
    return summa

#print(merge(nums), factorial(nums))

def triple(nums):
    nums_1 = []
    for i in nums:
        for j in nums:
            for k in nums:
                smth = i + j + k
                nums_1.append(smth)
    return nums_1

#print(len(triple(nums)), triple(nums))

def binary_search(nums, element, start, end, k):
    if start > end:
        k += 2
        return -1

    mid = (start + end) // 2
    if element == nums[mid]:
        k += 3
        return mid, k

    if element < nums[mid]:
        k += 2
        return binary_search(nums, element, start, mid-1, k)
    else:
        k += 2
        return binary_search(nums, element, mid+1, end, k)


sorted_nums = sorted(nums)
desired = [sorted_nums[randint(0, len(nums)-1)] for i in range(3)]
#for j in desired:
    #print('Индекс загаданного числа в списке =', binary_search(sorted_nums, j, 0, len(nums)-1, 0), 'Было загадано число', nums[binary_search(sorted_nums, j, 0, len(nums)-1), 0])

# Task 3

ex = []
def Sl1(ex):
    k = 0
    v = ex
    k += 1
    return k

y1 = []
for i in range(10):
    #print(len(ex), Sl1(ex))
    y1.append(Sl1(ex))
    ex.append(i)

chi = []

y2 = []
for i in range(10):
    chi.append(i)
    desired = randint(0, len(chi) - 1)
    #print(i + 1, binary_search(chi, desired, 0, len(chi)-1, 0)[1])
    y2.append(binary_search(chi, desired, 0, len(chi)-1, 0)[1])

def couple(nums):
    nums_1 = []
    k = 1
    for i in nums:
        k += 1
        for j in nums:
            smth = i + j
            nums_1.append(smth)
            k += 3
    return nums_1, k

chis = []
y3 = []
for i in range(10):
    chis.append(i)
    #print(len(chis), couple(chis)[1])
    y3.append(couple(chis)[1])

def Wow(chisl):
    copchi = []
    for i in chisl:
        copchi.append(i)
    newchisl = []
    summa = 0
    for i in range(2 ** len(copchi)):
        newchisl.append(summa + copchi[i])
        summa += copchi[i]
        copchi.append(summa)
    return len(newchisl)

chisl = [0]

y4 = []
for i in range(1, 10 + 1):
    chisl.append(i)
    y4.append(Wow(chisl))

import numpy as np
import matplotlib.pyplot as plt

fig = plt.subplots()

x = np.linspace(0, 10, 10)

plt.plot(x, y1)

plt.show()

plt.plot(x, y2)

plt.show()

plt.plot(x, y3)

plt.show()

plt.plot(x, y4)

plt.show()