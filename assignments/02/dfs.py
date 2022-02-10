res = []

# First input shows how many graphs
for _ in range(int(input())):
    graph = dict()

    # number of nodes for each instance
    num_nodes = int(input())
    all_nodes = []  # keeps track of non-connected nodes

    # turn input into dict of lists
    for _ in range(num_nodes):
        edges = input().split()
        node = edges[0]
        all_nodes.append(node)

        for edge in edges[1:]:
            # only need to add new edges, since it's not a directed graph
            if edge and edge not in all_nodes:
                # initialize adjacency list if doesn't exist
                if node not in graph:
                    graph[node] = [edge]
                else:
                    graph[node].append(edge)

    # start dfs
    to_visit = [all_nodes[0]]
    visited = []

    while len(visited) < num_nodes:
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
            if search_element in graph:
                to_visit = graph[search_element] + to_visit

    res.append(visited)

for graph in res:
    print(" ".join(graph))
