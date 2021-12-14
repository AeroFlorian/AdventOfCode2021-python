input="""start-YA
ps-yq
zt-mu
JS-yi
yq-VJ
QT-ps
start-yq
YA-yi
start-nf
nf-YA
nf-JS
JS-ez
yq-JS
ps-JS
ps-yi
yq-nf
QT-yi
end-QT
nf-yi
zt-QT
end-ez
yq-YA
end-JS"""

input_test = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

def find_path(place, path, graph):
    if place == 'end':
        return 1
    res = 0
    for x in graph[place]:
        if x.isupper() or x not in path:
            path_next = path.copy()
            path_next.append(x)
            res += find_path(x, path_next, graph)
    return res

def first_star():
    input_list = input.split('\n')
    graph = {}
    for x in input_list:
        y = x.split('-')
        if y[0] not in graph.keys():
            graph[y[0]] = []
        graph[y[0]].append(y[1])
        if y[1] not in graph.keys():
            graph[y[1]] = []
        graph[y[1]].append(y[0])
    print(f"First star: {find_path('start', ['start'], graph)}")

def find_path2(place, path, graph, already2):
    if place == 'end':
        return 1
    res = 0
    for x in graph[place]:
        if x.isupper() or x not in path:
            path_next = path.copy()
            path_next.append(x)
            res += find_path2(x, path_next, graph, already2)
        elif not already2 and x != 'start':
            path_next = path.copy()
            path_next.append(x)
            res += find_path2(x, path_next, graph, True)
    return res

def second_star():
    input_list = input.split('\n')
    graph = {}
    for x in input_list:
        y = x.split('-')
        if y[0] not in graph.keys():
            graph[y[0]] = []
        graph[y[0]].append(y[1])
        if y[1] not in graph.keys():
            graph[y[1]] = []
        graph[y[1]].append(y[0])
    print(f"Second star: {find_path2('start', ['start'], graph, False)}")



if __name__ == '__main__':
   first_star()
   second_star()

