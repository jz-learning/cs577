def intersect(n, q, p, pair):
    print(q)
    print(p)
    print(list(pair))
    return


def main():
    # number of test cases
    instance = int(input())

    res = ""
    for _ in range(instance):
        n = int(input())  # length of q or p
        q, p = [], []

        # sanitize input
        for _ in range(n):
            q.append(int(input()))

        for _ in range(n):
            p.append(int(input()))

        pair = zip(q, p)

        count = intersect(n, q, p, pair)
        res += f"{count}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
