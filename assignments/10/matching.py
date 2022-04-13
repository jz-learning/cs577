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
        graph = [tuple(map(int, input().split())) for _ in range(q)]

        # call to algo
        value = matching(m, n, q, graph)
        res += f"{value}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
