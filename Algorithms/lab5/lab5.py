# Task 2
import random

'''graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
    5: []
}

visited = [False] * len(graph)

def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return

components = 0
for j in range(len(graph)):
    if visited[j] == False:
        components += 1
        dfs(graph, j, visited)

print(components)

n = 7
matrix = [[1 if random.random() < 0.2 else 0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            matrix[i][j] = 1

start = random.randint(1, n-1)
finish = random.randint(1, n-1)

nums_start = n * start
nums_finish = n * finish + n - 1

matrix[start][0] = 0
matrix[finish][n-1] = 0

graph = {a: [] for a in range(n**2)}

for i in range(1, n-1):
    for j in range(n-1):
        if matrix[i][j] == 0:
            if matrix[i+1][j] == 0:
                graph[n*i+j].append((i+1)*n + j)
            if matrix[i-1][j] == 0:
                graph[n*i+j].append((i-1)*n + j)
            if matrix[i][j+1] == 0:
                graph[n*i+j].append(i*n + j+1)

def bfs(start, finish, graph):
    queue = [start]
    visited = []
    while len(queue) != 0:
        if queue[0] == finish:
            return True
        else:
            visited.append(queue[0])
            for i in graph[queue[0]]:
                if not(i in visited):
                    queue.append(i)
            queue.pop(0)
    return False

for i in matrix:
    print(i)

print(nums_start, nums_finish, bfs(nums_start, nums_finish, graph))'''

# Task 3

n = 10
matrix = [[1 if random.random() < 0.2 else 0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            matrix[i][j] = 1

start = random.randint(1, n-1)
finish = random.randint(1, n-1)

nums_start = n * start
nums_finish = n * finish + n - 1

matrix[start][0] = 0
matrix[finish][n-1] = 0

graph = {a: [] for a in range(n**2)}

for i in range(1, n-1):
    for j in range(n-1):
        if matrix[i][j] == 0:
            if matrix[i+1][j] == 0:
                graph[n*i+j].append((i+1)*n + j)
            if matrix[i-1][j] == 0:
                graph[n*i+j].append((i-1)*n + j)
            if matrix[i][j+1] == 0:
                graph[n*i+j].append(i*n + j+1)

def dfs(start, finish, graph):
    queue = [start]
    visited = []
    while len(queue) != 0:
        if queue[0] == finish:
            visited.append(queue[0])
            return visited
        else:
            visited.append(queue[0])
            for i in graph[queue[0]]:
                if not(i in visited):
                    queue[0] = i
    return False

for i in matrix:
    print(i)

print(dfs(nums_start, nums_finish, graph))
