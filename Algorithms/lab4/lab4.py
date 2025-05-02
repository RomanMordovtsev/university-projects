
def comb(nums):
    k = len(nums)-1
    while k >= 0:
        for i in range(0,len(nums)-k):
            if nums[i] > nums[i + k]:
                nums[i],nums[i+k] = nums[i+k],nums[i]
        k -= 1
    return nums

def quick(nums):
    if len(nums) <2:
        return nums
    m = (len(nums) - 1)//2
    l_nums = []
    r_nums = []
    i = 0
    while i < len(nums):
        if i != m:
            if nums[i] <= nums[m]:
                l_nums.append(nums[i])
            else:
                r_nums.append(nums[i])
        i += 1
    return quick(l_nums) + [nums[m]] + quick(r_nums)

def bucket(nums):
    if len(nums) < 2 or max(nums) == min(nums):
        return quick(nums)
    median = 0
    for i in nums:
        median += i
    median = median/len(nums)
    low_nums = []
    high_hums = []
    for j in nums:
        if j <= median:
            low_nums.append(j)
        else:
            high_hums.append(j)
    return bucket(low_nums) + bucket(high_hums)

def siftDown(nums, i):
    while i*2 + 1 < len(nums):
        left = 2*i + 1
        right = 2*i + 2
        j = left
        if right < len(nums) and nums[right] > nums[left]:
            j = right
        if nums[j] < nums[i]:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i = j
    return nums

def heap_builder(nums):
    i = len(nums)//2
    while i >= 0:
        siftDown(nums,i)
        i -= 1

def heap_sort(nums):
    heap_builder(nums)
    for i in range(0, len(nums)):
        nums = siftDown(nums[:len(nums)-i:],0) + nums[len(nums)-i::]
        nums[0], nums[len(nums)-i-1] = nums[len(nums) - i-1], nums[0]
    return nums

def heap_sort_wrong(nums):
    nums_1 = []
    heap_builder(nums)
    nums_1.append(nums[0])
    nums[0], nums[-1] = nums[-1], nums[0]
    nums.pop(-1)
    for i in range(len(nums)):
        siftDown(nums,0)
        nums_1.append(nums[0])
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop(-1)
    return nums_1