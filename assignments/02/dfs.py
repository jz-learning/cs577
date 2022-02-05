"""
2
3
A B
B A
C
9
1 2 9
2 3 5 6
3 2 7
4 6
5 2
6 2 4
7 3
8 9
9 1 8
"""

# how many graphs
instance = int(input())
res = []

for _ in range(instance):
    graph = dict()

    # number of edges for each instance
    num_edge = int(input())
    all_nodes = []

    # turn input into dict of lists
    for _ in range(num_edge):
        edge = input().split()
        all_nodes.append(edge[0])
        graph[edge[0]] = edge[1:]

    # start bfs
    first_ele = list(graph.keys())[0]
    to_visit = [first_ele]
    visited = []

    while to_visit or all_nodes:
        # pops the first element of the list
        if to_visit:
            search_element = to_visit.pop(0)
        else:
            to_visit.append(all_nodes.pop(0))
            continue

        # dfs logic, visit each node and add to stack
        if search_element not in visited:
            # mark as visited
            visited.append(search_element)
            # this is to keep the lexicographic ordering of each edge list
            to_visit = graph[search_element] + to_visit

    res.append(visited)

for graph in res:
    print(" ".join(graph))
