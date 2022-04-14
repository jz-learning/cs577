from collections import defaultdict


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # Using BFS as a searching algorithm
    def BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying ford fulkerson algorithm
    def match(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def matching(m, n, q, graph):
    return m, n, q, graph


def main():
    # number of test cases
    instance = int(input())
    res = ""

    for _ in range(instance):
        """
        m - nodes in A
        n - nodes in B
        q - edges
        """
        m, n, q = map(int, input().split())
        nodes = m + n + 2

        matrix = [[0] * nodes for _ in range(nodes)]
        # print(matrix)
        for _ in range(q):
            i, j = tuple(map(int, input().split()))
            # print(i, j)
            matrix[i][j + m] = 1
        # print(matrix)

        for i in range(1, m + 1):
            matrix[0][i] = 1
        for i in range(m + 1, nodes):
            matrix[i][nodes - 1] = 1
        # print(matrix)

        flow = Graph(matrix)
        maxFlow = flow.match(0, nodes - 1)
        perfect = "N"
        if maxFlow == n:
            perfect = "Y"

        res += f"{maxFlow} {perfect}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
