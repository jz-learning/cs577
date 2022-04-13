def flow():
    return 1


def main():
    # number of test cases
    instance = int(input())
    res = ""

    for _ in range(instance):
        items = []
        # num nodes and edges
        n, e = map(int, input().split())

        for _ in range(e):
            src, dst, cap = map(int, input().split())
            # print(src, dst, cap)

        ans = flow()
        res += f"{ans}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
