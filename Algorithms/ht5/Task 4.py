count = 0

steps = [1, 2, 3]
n = 10
while len(steps) < n:
    i = len(steps) - 1
    steps.append(steps[i-1] + steps[i-2] + steps[i-3])

print(steps[-1])