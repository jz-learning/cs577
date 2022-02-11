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
    S = [list(map(int, input().split())) for _ in range(num_inter)]

    # Sort based on end time
    intervals = sorted(S, key=lambda a: a[1])

    jobs = 1
    prev = intervals[0][1]
    print(intervals)
    for i in range(1, len(intervals)):
        if intervals[i][0] >= prev:
            print(f"{intervals[i]} bigger than {intervals[i - 1]}")
            print(f"taking the job{intervals[i]}")
            prev = intervals[i][1]
            jobs += 1

    res.append(f"{jobs}")


for n in res:
    print(n)
