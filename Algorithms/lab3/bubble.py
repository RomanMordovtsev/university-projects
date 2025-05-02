from random import randint

nums = [randint(-100,100) for i in range(10)]
def bubble(nums):
    for i in range(0,len(nums)-1):
       for j in range(0, len(nums)-1 - i):
           if nums[j] > nums[j + 1]:
               nums[j], nums[j+1] = nums[j + 1], nums[j]
    return nums

def linear(nums):
    div_0 = 0
    div_1 = 0
    div_2 = 0
    for i in nums:
        if i%3 == 0:
            div_0 += 1
    for j in nums:
        if j%3 == 1:
            div_1 += 1
    for k in nums:
        if k%3 == 2:
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
        while l < len(left) and r<len(right):
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

#merge(nums)
#print(nums)

def factorial(nums):
    summa = 0
    k = 0
    while k < len(nums):
        for i in range(k,len(nums)):
            summa += nums[i]
        k += 1
    return summa

#print(factorial(nums))

def triple(nums):
    nums_1 = []
    for i in nums:
        for j in nums:
            for k in nums:
                smth = i + j + k
                nums_1.append(smth)
    return nums_1

#print(triple(nums))

def binary_search(nums, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == nums[mid]:
        return mid

    if element < nums[mid]:
        return binary_search(nums, element, start, mid-1)
    else:
        return binary_search(nums, element, mid+1, end)


sorted_nums = sorted(nums)
desired = [sorted_nums[randint(0,len(nums)-1)] for i in range(3)]
for j in desired:
    print(binary_search(sorted_nums, j, 0, len(nums)-1))






