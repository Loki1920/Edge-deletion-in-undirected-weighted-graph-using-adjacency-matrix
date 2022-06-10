# Edge deletion in  undirected weighted graph using adjacency matrix
nodes = []
node_count = 0
graph = []

def add_node(v):
    global nodes,node_count,graph
    if v in nodes:
        print(v,"is already present in ",nodes)
    else:
        node_count = node_count +1
        nodes.append(v)
        for j in graph:
            j.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,e):
    global graph
    if v1 not in nodes:
        print("No")
    elif v2 not in nodes:
        print("No")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = e
        graph[index2][index1] = e

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not in graph")
    else:
        index1 = nodes.index(v)
        node_count -= 1
        nodes.remove(v)
        graph.pop(index1)
        for n in graph:
            n.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in graph.")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end = " ")
        print()


add_node("A")
add_node("B")
add_node("C")

add_edge("A","B",10)
add_edge("B","C",7)
add_edge("A","C",5)

print("graph before deleting:\n")
print_graph()

delete_edge("A","B")

print("graph after deleting a edge")
print_graph()
