import math

# adjacency_matrix = [[math.inf, 3, 1, 3, math.inf, math.inf],
#                     [3, math.inf, 4, math.inf, math.inf, math.inf],
#                     [1, 4, math.inf, math.inf, 7, 5],
#                     [3, math.inf, math.inf, math.inf, math.inf, 2],
#                     [math.inf, math.inf, 7, math.inf, math.inf, 4],
#                     [math.inf, math.inf, 5, 2, 4, math.inf]]

class Graph:
    def __init__(self, name):
        self.Nodes = {}
        self.Name = name

    def GetNodes(self):
        return self.Nodes

    def SetNode(self, nodes):
        for i in nodes:
            self.Nodes[i[0]] = i[1]

    def AdjacencyMatrixBuilder(self, nodes):
        N = len(nodes)
        adjacencyMatrix = []
        for i in range(N):
            currentNodes = nodes[i].GetNodes()
            currentMatrix = []
            for j in range(N):
                if j in currentNodes.keys():
                    currentMatrix.append(currentNodes[j])
                else:
                    currentMatrix.append(math.inf)
            adjacencyMatrix.append(currentMatrix)
        return adjacencyMatrix

dot0 = Graph("Белгород")
dot_0 = [[1, 172], [2, 36], [3, 120], [4, 152], [5, 11]]

dot1 = Graph("Алексеевка")
dot_1 = [[0, 172], [2, 152], [3, 154], [4, 78], [5, 175]]

dot2 = Graph("Шебекино")
dot_2 = [[0, 36], [1, 152], [3, 131], [4, 113], [5, 25]]

dot3 = Graph("Губкин")
dot_3 = [[0, 120], [1, 154], [2, 131], [4, 164], [5, 128]]

dot4 = Graph("Валуйки")
dot_4 = [[0, 152], [1, 78], [2, 113], [3, 164], [5, 137]]

dot5 = Graph("Разумное")
dot_5 = [[0, 11], [1, 175], [2, 25], [3, 128], [4, 137]]


test_array = [dot0, dot1, dot2, dot3, dot4, dot5]
test_array_1 = [dot_0, dot_1, dot_2, dot_3, dot_4, dot_5]
for i in range(len(test_array)):
    test_array[i].SetNode(test_array_1[i])



adjacency_matrix = Graph("начало").AdjacencyMatrixBuilder(test_array)

town_name = {0: "Белгород", 1: "Алексеевка", 2: "Шебекино", 3: "Губкин", 4: "Валуйки", 5: "Разумное"}

print(f"Расстояние от населенного пункта {test_array[0].Name}")

N = len(adjacency_matrix)
used = [0]
table = [[]]
for i in range(N):
    if adjacency_matrix[0][i] == 0:
        table[0].append(math.inf)
    else:
        table[0].append(adjacency_matrix[0][i])
count = 1
used = [0]
for i in range(1, N):
    current = table[i-1].index(min(table[i-1]))
    current_len = table[i-1][current]
    print(f"точка: {town_name[current]}, длина пути {current_len}")
    used.append(current)
    new_table = []
    #print("used: ", used)
    for j in range(N):
        if j in used:
            new_table.append(math.inf)
        else:
            new_table.append(min(table[i-1][j], adjacency_matrix[current][j] + current_len))
    table.append(new_table)
