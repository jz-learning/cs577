res = ""

# First input shows how many instances
for _ in range(int(input())):
    # number of total intervals
    num_inter = int(input())

    # turn input into lists of lists
    S = [list(map(int, input().split())) for _ in range(num_inter)]

    # Sort based on end time
    intervals = sorted(S, key=lambda a: a[1])

    # initialize the first interval
    jobs = 1
    prev = intervals[0][1]

    for i in range(1, len(intervals)):
        # cheking compatibility, then update
        if intervals[i][0] >= prev:
            prev = intervals[i][1]
            jobs += 1

    res += f"{jobs}\n"

print(res[:-1])
