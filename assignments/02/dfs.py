# how many graphs
instance = int(input())
res = []

for _ in range(instance):
    graph = dict()

    # number of edges for each instance
    num_edge = int(input())
    all_nodes = []  # keeps track of non-connected nodes

    # turn input into dict of lists
    for _ in range(num_edge):
        edge = input().split()
        all_nodes.append(edge[0])
        graph[edge[0]] = edge[1:]

    # start dfs
    to_visit = [all_nodes[0]]
    visited = []

    while to_visit or all_nodes:
        # pops the first element of the list
        if to_visit:
            search_element = to_visit.pop(0)
        else:
            search_element = all_nodes[0]

        # dfs logic, visit each node and add to stack
        if search_element not in visited:
            # mark as visited
            visited.append(search_element)
            all_nodes.remove(search_element)

            # this is to keep the lexicographic ordering of each edge list
            to_visit = graph[search_element] + to_visit

    res.append(visited)

for graph in res:
    print(" ".join(graph))
