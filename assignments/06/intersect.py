def merge(front, back):
    merged, intersects = [], 0
    i, j = 0, 0
    l, r = len(front), len(back)

    while i < l and j < r:
        f, b = front[i], back[j]
        if f[1] > b[1]:
            merged.append(b)
            intersects += l - i
            j += 1
        else:
            merged.append(f)
            i += 1

    if j == r:
        merged.extend(front[i:])
    elif i == l:
        merged.extend(back[j:])

    return merged, intersects


def intersect(n, pairs):
    # base case
    if n == 1:
        return (pairs, 0)

    mid = n // 2

    front = pairs[:mid]
    back = pairs[mid:]

    A, ctA = intersect(mid, front)
    B, ctB = intersect(n - mid, back)

    C, ctC = merge(A, B)

    return C, ctA + ctB + ctC


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

        # combine the list of q and p so they can be sorted together
        pairs = list(zip(q, p))

        # sort the two respective lists together by Q
        pairs = sorted(pairs, key=lambda pair: pair[0])

        _, count = intersect(n, pairs)
        res += f"{count}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
