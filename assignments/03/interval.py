res = []

# First input shows how many instances
for _ in range(int(input())):
    # number of total intervals
    num_inter = int(input())

    # edge case
    if num_inter < 1:
        res.append(0)
        continue

    # turn input into lists of lists
    S = [input().split() for _ in range(num_inter)]

    # Sort based on end time
    intervals = sorted(S, key=lambda a: a[1])

    jobs = 1

    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[i - 1][1]:
            jobs += 1

    res.append(f"{jobs}")


for n in res:
    print(n)
